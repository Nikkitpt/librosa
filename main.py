import librosa
import librosa.display
import numpy as np

def rms_audio_level(audio_file):
    # Gets autdio data
    audio_data, sample_rate = librosa.load(audio_file, sr=None, mono=True)

    # Calculate the RMS level
    rms = np.sqrt(np.mean(audio_data ** 2))

    return rms

if __name__ == "__main__":
    audio_file = "sample.wav"  

    rms_level = rms_audio_level(audio_file)
    print(f"RMS Audio Level: {rms_level} dB")
