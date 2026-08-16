# 🧠 EEG based classification of Digit-Span Memorization vs. Listening

## Instructions

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
