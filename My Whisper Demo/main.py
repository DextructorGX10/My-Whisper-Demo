import whisper

model = whisper.load_model("base")
result = model.transcribe("voice.mp3")

print(result)

with open("transcription.txt", "w") as f:
    f.write(result["text"])

