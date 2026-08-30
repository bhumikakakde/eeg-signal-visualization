import mne
from mne.datasets import eegbci
import matplotlib.pyplot as plt

# Download and load real EEG data (subject 1, run 1 — eyes open baseline)
raw_fname = eegbci.load_data(subjects=1, runs=[1])[0]
raw = mne.io.read_raw_edf(raw_fname, preload=True)

# --- Preprocessing: bandpass filter (removes drift and high-frequency noise) ---
raw.filter(l_freq=1.0, h_freq=40.0)

# Extract data and time information
data = raw.get_data()
times = raw.times
channel_names = raw.ch_names

print("Channel names:", channel_names)

# Select channels to plot (first 10 channels)
num_channels_to_plot = 10
selected_channels = range(num_channels_to_plot)

# Select the first 5 seconds of data
sampling_rate = raw.info['sfreq']
num_samples = int(5 * sampling_rate)
data_segment = data[:, :num_samples]
times_segment = times[:num_samples]

# --- Time-domain plot ---
plt.figure(figsize=(12, 15))
for i, channel_index in enumerate(selected_channels):
    ax = plt.subplot(num_channels_to_plot, 1, i + 1)
    plt.plot(times_segment, data_segment[channel_index, :])
    plt.title(channel_names[channel_index], loc='left', fontsize=10)
    plt.ylabel('µV', fontsize=8)

plt.xlabel('Time (s)', fontsize=10)
plt.tight_layout()
plt.show()

# --- Frequency-domain analysis: Power Spectral Density ---
raw.compute_psd().plot()
plt.show()