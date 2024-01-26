# Predict Heart Attack with Regression 

This Python prjoect uses different Regression Methods to predict Heart Failure using a Dataset provided from kaggle.com 

## Description
Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of 5CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help

## Table of Contents

- [Dataset](#requirements)
- [Requirements](#requirements)
- [Notebook](#notebook-contents)
- [License](#license)

## Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/data) and includes key features such as:

- **Age**: Age of the patient [years]
- **Sex**: Sex of the patient [M: Male, F: Female]
- **ChestPainType**: Chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
- **RestingBP**: Resting blood pressure [mm Hg]
- **Cholesterol**: Serum cholesterol [mm/dl]
- **FastingBS**: Fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
- **RestingECG**: Resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
- **MaxHR**: Maximum heart rate achieved [Numeric value between 60 and 202]
- **ExerciseAngina**: Exercise-induced angina [Y: Yes, N: No]
- **Oldpeak**: Oldpeak = ST [Numeric value measured in depression]
- **ST_Slope**: The slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
- **HeartDisease**: Output class [1: heart disease, 0: Normal]


## Notebook

## Requirements
```bash
pip install pandas
pip install numpy
pip install scikit-learn
```
## License
- [NumPy](https://numpy.org): A open-source library for numerical computing in Python.
- [Matplotlib](https://matplotlib.org): A open-source plotting library for Python. License.
- [Pandas](https://pandas.pydata.org/): A open-source library for Data Science.
