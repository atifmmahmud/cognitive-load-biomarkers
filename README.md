# 🧠 EEG based classification of Digit-Span Memorization vs. Listening

## Welcome!
In this project I sought to develop a model that uses electroenephelography (EEG) signals to classify between memorization and listening during a digit span task. This served as a first step towards evaluating the feasibility of using EEG signals in determining cognitive load and supporting the advancement of wearable-based cognitive monitoring.  
  
I used an available OpenNeuro dataset (Pavlov et al., 2024) for my analysis. The dataset contains 64-channel electroencephalography (EEG), electrocardiography (ECG), photoplethysmography (PPG), and pupillometry data from 86 participants during rest (eyes-closed) and a working-memory task (digit-span with series recall).  

[YouTube Video](https://youtu.be/dh5WUA-YOuc)

## Try it!

### Step 1
Clone this repository
```
git clone https://github.com/atifmmahmud/cognitive-load-biomarkers.git
```

### Step 2
Download the data from [this Google Drive folder](https://drive.google.com/drive/folders/1sJpfs5JYOIJSlfUAt9Lu1buifXTB_5Uf?usp=drive_link). Make sure the `data/` folder is saved at the same level as the notebook. 

```text
|--- .gitignore
|--- eeg-classifier.ipynb
|--- ica-log.txt
|--- README.md
|--- requirements.txt
|--- data/ <========================= This is the folder to download from Google Drive
        |---.bidsignore
        |--- CHANGES
        |--- dataset_description.json
        |--- eeg-power-features-per-roi-no-baseline.csv
        |--- eeg-power-features-per-roi.csv
        |--- eeg-power-features.csv
        |--- participants.json
        |--- participants.tsv
        |--- README
        |--- filtered-referenced-eeg/
        |--- ica-excluded-eeg/
        |--- stimuli/
        |--- sub-032/
        |--- sub-033/
        | <--- folders for all other participants --->
```

### Step 3
Install the requirements
```
pip install -r requirements.txt
```

## Acknowledgements
I am using data from OpenNeuro dataset 003838  
  
Yuri G. Pavlov, Dauren Kasanov, Alexandra I. Kosachenko, and Alexander I. Kotyusov (2024). EEG, pupillometry, ECG and photoplethysmography, and behavioral data in the digit span task and rest. OpenNeuro. [Dataset] doi: doi:10.18112/openneuro.ds003838.v1.0.6  
https://doi.org/10.1038/s41597-022-01414-2
