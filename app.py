## Our streamlit app
import streamlit as st
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV, LeaveOneGroupOut
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

if "scores_df" not in st.session_state:
    st.session_state.scores_df = pd.DataFrame(columns=["model", "metric", "score"])

st.title("EEG based classification of cognitive load/task")
st.subheader("Created by")
st.write("Atif Mahmud")
st.subheader("About")
st.write("In this project I sought to develop a model that uses electroenephelography (EEG) signals to classify between memorization and listening during a digit span task. This served as a first step towards evaluating the feasibility of using EEG signals in determining cognitive load and supporting the advancement of wearable-based cognitive monitoring. I used an available OpenNeuro dataset (Pavlov et al., 2024) for my analysis. The dataset contains 64-channel electroencephalography (EEG), electrocardiography (ECG), photoplethysmography (PPG), and pupillometry data from 86 participants during rest (eyes-closed) and a working-memory task (digit-span with series recall).")
st.subheader("Acknowledgements")
st.write("Yuri G. Pavlov, Dauren Kasanov, Alexandra I. Kosachenko, and Alexander I. Kotyusov (2024). EEG, pupillometry, ECG and photoplethysmography, and behavioral data in the digit span task and rest. OpenNeuro. [Dataset] doi: doi:10.18112/openneuro.ds003838.v1.0.6")

with st.sidebar:
    selected_dataset = st.selectbox("Select your dataset", 
    ["Whole Brain Power", "ROI specific power", "ROI specific power without baseline"])


st.subheader("The dataset")
if (selected_dataset):
    st.write("Selected ", selected_dataset)
    if selected_dataset == "Whole Brain Power":
        df = pd.read_csv("streamlit-data/eeg-power-features.csv")
    elif selected_dataset == "ROI specific power":
        df = pd.read_csv("streamlit-data/eeg-power-features-per-roi.csv")
    else:
        df = pd.read_csv("streamlit-data/eeg-power-features-per-roi-no-baseline.csv")

st.dataframe(df)

def run_random_forest(X, Y, group, n_estimators, max_depth, min_samples_split, min_samples_leaf):
    with st.spinner("Running random forest..", show_time=True):
        logo = LeaveOneGroupOut()
        accuracies, true, predicted = [], [], []
        feature_importances = []

        for train, test in logo.split(X, Y, groups=group):
            classifier = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, random_state=42, class_weight="balanced")
            classifier.fit(X.iloc[train], Y.iloc[train])
            prediction = classifier.predict(X.iloc[test])
            accuracy = accuracy_score(Y.iloc[test], prediction)
            accuracies.append(accuracy)
            true.extend(Y.iloc[test])
            predicted.extend(prediction)
            feature_importances.append(classifier.feature_importances_)

        mean = np.mean(feature_importances, axis=0)
        stddev = np.mean(feature_importances, axis=0)

        st.metric("Mean accuracy", f"{np.mean(accuracies)}")
        report_dict = classification_report(true, predicted, output_dict=True)
        feature_importances_df = pd.DataFrame({
            "feature" : X.columns,
            "mean" : mean,
            "std. dev" : stddev
        })
        st.subheader("Classification report")
        st.dataframe(report_dict)
        st.subheader("Feature importances")
        st.dataframe(feature_importances)
        report = classification_report(true, predicted, output_dict = True)
        report_df = pd.DataFrame(report).transpose().round(3)

        st.subheader("This model's scores")
        st.dataframe(pd.DataFrame(report_df))

        st.session_state.scores_df.loc[len(st.session_state.scores_df)] = [selected_dataset + " " + Y.name, "accuracy", accuracy]
        st.session_state.scores_df.loc[len(st.session_state.scores_df)] = [selected_dataset + " " + Y.name, "f1_macro", report_df.loc["macro avg", "f1-score"]]
        st.session_state.scores_df.loc[len(st.session_state.scores_df)] = [selected_dataset + " " + Y.name, "f1_weighted", report_df.loc["weighted avg", "f1-score"]]

        st.subheader("All model scores")
        st.dataframe(st.session_state.scores_df)

        st.subheader("Comparing models")
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.barplot(x="metric", y="score", hue="model", data=st.session_state.scores_df, palette="coolwarm", ax=ax)
        ax.set_title("Comparing performance metrics of our models")
        ax.set_xlabel("Metric")
        ax.set_ylabel("Score")
        ax.axhline(0.5)
        ax.set_ylim(0, 1)
        st.pyplot(fig)

    st.success("Done!")

with st.sidebar:
    st.subheader("Let's run our model!")
    Y_selected = st.selectbox("Pick your Y", ["correct (memory only)", "condition", "load"])
    st.selectbox("Pick your model", ["Random Forest"])
    n_estimators = st.slider("Number of estimators", 50, 500, step=50)
    max_depth = st.slider("Maximum depth", 10, 50, step=5)
    min_samples_split = st.slider("Minimum samples to split", 2, 30, step=2)
    min_samples_leaf = st.slider("Minimum samples required to be leaf", 2, 50, step=2)

    if selected_dataset == "Whole Brain Power":
        X = df[["alpha_power", "gamma_power"]]
    else:
        X = df[["frontal_alpha", "frontal_gamma",
            "parietal_alpha", "parietal_gamma",
            "temporal_alpha", "temporal_gamma",
            "midline_alpha", "midline_gamma"
        ]]
    group = df["participant"]
    if Y_selected == "correct (memory only)":
        Y_selected = "correct"
    Y = df[Y_selected]

    if Y_selected == "correct":
        memory_only = df[df["condition"] == "Memory"].copy()
        if selected_dataset == "Whole Brain Power":
            X = memory_only[["alpha_power", "gamma_power"]]
        else:
            X = memory_only[["frontal_alpha", "frontal_gamma",
                "parietal_alpha", "parietal_gamma",
                "temporal_alpha", "temporal_gamma",
                "midline_alpha", "midline_gamma"
            ]]
        Y = memory_only["correct"]
        group = memory_only["participant"]

    st.button("Run model!", on_click=run_random_forest,
                            args=(X, Y, group, n_estimators, max_depth, min_samples_split, min_samples_leaf))
