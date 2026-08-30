  # EEG Signal Visualization

  A Python pipeline for loading, filtering, and visualizing EEG signals using MNE-Python.

  ## Features
  - Loads real EEG data from the PhysioNet EEG Motor Movement/Imagery dataset
  - Applies a bandpass filter (1–40 Hz) for preprocessing
  - Visualizes raw EEG channels in the time domain
  - Computes and plots Power Spectral Density (PSD) for frequency-domain analysis

  ## Requirements
  - Python 3.x
  - mne
  - matplotlib

  Install dependencies:


  
   ## Example Output

   **Time-domain EEG channels:**
   ![Time domain plot](time_domain_plot.png)

   **Power Spectral Density:**
   ![PSD plot](psd_plot.png)
