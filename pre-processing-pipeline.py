# data loading and preparation
raw = mne.io.read_raw_edf(psg_files[0], preload=True)
hypnogram = mne.read_annotations(hypno_files[0])
raw.set_annotations(hypnogram)

# Select EEG chanels only
# remove all other waves such as EMG, EOG, ECG
eeg_channels = mne.pick_types(raw.info, eeg=True)
raw.pick(eeg_channels)

# Bandpass filtering
# Muscle moment have above 40 hz and eye blinks below 0.5 hz. Therefore selected
#range for EEG signal are 0.5 - 40
raw.filter(0.5, 40)

# Segmentation
# since EEG is a large file we create small chunks 
events, event_ids = mne.events_from_annotations(raw)
epochs = mne.Epochs(raw, events, event_id=event_ids,tmin=0, tmax=30,baseline=None, preload=True)

# extract data labels
X = epochs.get_data()
y = epochs.events[:, -1]

# Add chanel dimentions for CNN
X = X[..., np.newaxis]

# Normalizing 
X = (X - np.mean(X, axis=2, keepdims=True)) / (np.std(X, axis=2, keepdims=True) + 1e-5)

