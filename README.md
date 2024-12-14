# README.md

## Instructions for Setup and Installation
1. Ensure Python 3.8 or higher is installed on your system.
2. Install the required dependencies using the following command:
    ```
    pip install -r requirements.txt
    ```
3. Make sure FFmpeg is installed and added to your system PATH.

## Guide to Running the Script
1. Place the audio file you want to transcribe in the root directory of the project under the name `input_audio.wav`.
2. Place the reference transcription file in the root directory of the project under the name `ground_truth.txt`.
3. Run the script using the command:
    ```
    python transcribe.py
    ```
4. After the script finishes execution:
    - The transcription will be saved in the file `transcription.txt`.
    - The performance metrics will be logged in the file `metrics.log`.

## Audio Preprocessing

Before transcription, input audio is preprocessed to ensure compatibility with the Whisper model. This includes:

- **Resampling**: Adjusting the sampling rate to 16 kHz, if necessary.
- **Mono Conversion**: Converting stereo audio to mono, if necessary.
- **Format Check**: Ensuring the audio is in WAV format.

These steps ensure the audio signal is optimized for reliable transcription and accurate results without the need for intermediate files.


## Explanation of Metrics
- **Latency (Transcription Time):** 
  - This is the time taken by the model to process and transcribe the input audio. It is measured in seconds and logged in `metrics.log`.
- **WER (Word Error Rate):** 
  - A metric that shows the percentage of errors in the transcription compared to the reference transcription. 
  - The formula for WER is:
    ```
    WER = (S + D + I) / N
    ```
    Where:
    - `S` = Number of substitutions,
    - `D` = Number of deletions,
    - `I` = Number of insertions,
    - `N` = Total number of words in the reference transcription.
  - A lower WER indicates a better match between the transcribed text and the reference.

## Metrics Logged
### Example Metrics (from `metrics.log`)


- **Transcription Time:** `30.84 seconds`
  - Indicates the time taken to process and transcribe `input_audio.wav`.
- **WER:** `0.16`
  - Indicates that 16% of the words in the transcription differ from the reference transcription.

## Observations
The transcription was completed in a reasonable amount of time (`30.84 seconds`), and the WER of `0.16` demonstrates a good alignment between the transcribed output and the ground truth.

