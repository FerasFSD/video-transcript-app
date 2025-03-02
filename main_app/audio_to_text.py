import whisper
import os

def transcribe_audio(audio_path, model_name="medium"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result["text"]

def save_transcription(text, output_path):
    """Speichert Transkription als TXT"""
    with open(output_path, "w") as f:
        f.write(text)
    return output_path