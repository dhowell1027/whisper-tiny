import whisper

# Load the Whisper Tiny model
model = whisper.load_model("tiny")

# Transcribe an audio file
result = model.transcribe("sample_audio.mp3")

# Print the transcription
print("Transcription:", result["text"])
