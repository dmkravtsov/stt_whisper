# import subprocess
# import sys

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# install('git+https://github.com/openai/whisper.git')
# install('jiwer')
# install('numpy<=1.26')


import time
import logging
import whisper
from jiwer import wer
import librosa
import numpy as np

def preprocess_audio(input_file, target_sample_rate=16000):
    """
    Checks if the audio file meets the requirements and processes it in memory.
    - Target sample rate: 16 kHz
    - Channels: Mono

    Arguments:
    - input_file: Path to the input audio file.
    - target_sample_rate: Desired sample rate for the audio.

    Returns:
    - Preprocessed audio as a NumPy array and its sample rate.
    """
    try:
        # Load the audio file
        audio, sample_rate = librosa.load(input_file, sr=None, mono=True)

        # Resample if necessary
        if sample_rate != target_sample_rate:
            print(f"Resampling audio from {sample_rate} Hz to {target_sample_rate} Hz")
            audio = librosa.resample(audio, orig_sr=sample_rate, target_sr=target_sample_rate)

        print("Audio preprocessing completed.")
        return audio, target_sample_rate
    except Exception as e:
        print(f"Error during audio preprocessing: {e}")
        return None, None

# Set up logging configuration to log results in a file
logging.basicConfig(filename="metrics.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load the Whisper model
model = whisper.load_model("base")

# Specify the input audio file
input_audio_file = "input_audio.wav"

# Preprocess the audio file in memory
audio, sample_rate = preprocess_audio(input_audio_file)

if audio is not None:
    # Record the start time before transcription
    start_time = time.time()

    # Perform the transcription using Whisper model
    result = model.transcribe(audio=audio)

    # Record the end time after transcription
    end_time = time.time()

    # Calculate the transcription time (delay)
    transcription_time = end_time - start_time

    # Log the transcription time
    logging.info(f"Transcription time for {input_audio_file}: {transcription_time:.2f} seconds")

    # Get the transcribed text
    transcribed_text = result['text']

    # Save the transcribed text to a file
    with open("transcription.txt", "w") as transcription_file:
        transcription_file.write(transcribed_text)

    # Specify the ground truth file
    ground_truth_file = "ground_truth.txt"

    # Read the ground truth transcription
    with open(ground_truth_file, "r") as f:
        ground_truth = f.read()

    # Calculate Word Error Rate (WER) by comparing with ground truth
    error_rate = wer(ground_truth, transcribed_text)

    # Log the WER result
    logging.info(f"WER for {input_audio_file}: {error_rate:.2f}")

    # Print transcription and metrics
#     print("Transcribed Text:")
#     print(transcribed_text)
#     print(f"Transcription time: {transcription_time:.2f} seconds")
#     print(f"Word Error Rate (WER): {error_rate:.2f}")
# else:
#     print("Audio preprocessing failed. Please check the input file.")
