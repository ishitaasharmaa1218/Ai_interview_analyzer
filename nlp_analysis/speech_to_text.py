import whisper
import imageio_ffmpeg as ffmpeg

# Load model
model = whisper.load_model("base")

# Transcribe audio
result = model.transcribe("audio.mp3", fp16=False)

# Print output
print("Transcript:\n")
print(result["text"])

# ✅ ADD THIS PART (IMPORTANT)
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("\nTranscript saved successfully!")