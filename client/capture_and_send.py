"""Skeleton audio capture client for Raspberry Pi / Linux using sounddevice.

This script captures short audio chunks and saves them locally. Integration with backend STT via WebSocket or multipart upload
should be implemented on top of this skeleton.

CEO e criador: David Adriano Ferrari dos Santos
"""
import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000
DURATION = 5  # seconds per recording
FILENAME = "sample.wav"

if __name__ == "__main__":
    print("Recording", DURATION, "seconds...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    sf.write(FILENAME, audio, SAMPLE_RATE)
    print("Saved to", FILENAME)
