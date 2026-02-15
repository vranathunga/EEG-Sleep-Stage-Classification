# EEG-Sleep-Stage-Classification
This project was conducted to identify the EEG signal waves identification by using machine learning technologies.

<p align="left">
  <img src="images/banner.jpg" width="350" title="Iris Flower">
</p>

## Introduction :bulb:
In sleep the human brain goes through several stages such as 
- W - wake
- N1 - Light Sleep
- N2 - Stable Sleep
- N3 - Deep Sleep
- REM - Dreaming Stage

In this project I will train a model to predict the sleep stage based on a given signal.

## Dataset :bar_chart:
The dataset for this project was obtained from the Sleep-EDF database expanded on PhysioNet. PSG and corresponding hypnogram files were used in this study. URL to the website as follows. Total database size is 8 GB
- URL - https://physionet.org/content/sleep-edfx/1.0.0/

## Methodology :rocket:
Since the database is very huge I used a few files of that to train the model. I first used the random forest to train the model but with that the model showed a low accuracy such as 0.4275. After that I used the CNN to train the model and for that it showed 0.9048 accuracy. 

## Technologies :hammer_and_wrench:

- tensorflow
- numpy
- mne
- scikit-learn
- matplotlib
- streamlit

## EEG Pre-processing Pipeline :mag:
EEG signal is a signal captured during sleep for long hours such as up to 8 hours. They often contains much noise since it captures the muscle moments of the head and eye moments also. When we create a model we want to remove the noise and select only the EEG signals. Since it is a 8 hours long file we are breaking it to small chunks such as epochs. 

- Load raw EEG
- Load annotations
- Attach annotations
- Select EEG channels
- Bandpass filter (0.5–40 Hz)
- Segment into 30-second epochs
- Normalize epochs

