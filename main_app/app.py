import streamlit as st
import os
from main_app.video_to_audio import convert_video_to_audio
from main_app.audio_to_text import transcribe_audio, save_transcription
from main_app.text_extractor import extract_text_from_file
from main_app.utils.file_utils import clean_temp_files
import sys
from pathlib import Path

# Fügen Sie das Projektverzeichnis zum Python-Pfad hinzu
sys.path.insert(0, str(Path(__file__).parent.parent))
# Konfiguration
st.set_page_config(page_title="Multi-File Processor", layout="wide")

# Temporäre Ordner
AUDIO_TEMP_DIR = "temp_audio"
TEXT_TEMP_DIR = "temp_text"

def main():
    st.title("Multi-File Processing App")
    
    # Video zu Audio Converter
    with st.expander("Video to Audio Converter"):
        video_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
        if video_file:
            video_path = os.path.join(AUDIO_TEMP_DIR, video_file.name)
            with open(video_path, "wb") as f:
                f.write(video_file.getbuffer())
            audio_path = convert_video_to_audio(video_path)
            st.audio(audio_path)
            st.download_button("Download Audio", open(audio_path, "rb"), file_name=os.path.basename(audio_path))

    # Audio zu Text Transkription
    with st.expander("Audio to Text Transcription"):
        audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav"])
        if audio_file:
            audio_path = os.path.join(AUDIO_TEMP_DIR, audio_file.name)
            with open(audio_path, "wb") as f:
                f.write(audio_file.getbuffer())
            text = transcribe_audio(audio_path)
            text_path = save_transcription(text, os.path.join(TEXT_TEMP_DIR, "transcript.txt"))
            st.download_button("Download Transcript", open(text_path, "rb"), file_name="transcript.txt")

    # Text Extractor
    with st.expander("Text Extractor"):
        doc_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])
        if doc_file:
            file_path = os.path.join(TEXT_TEMP_DIR, doc_file.name)
            with open(file_path, "wb") as f:
                f.write(doc_file.getbuffer())
            text = extract_text_from_file(file_path)
            text_path = save_transcription(text, os.path.join(TEXT_TEMP_DIR, "extracted.txt"))
            st.download_button("Download Extracted Text", open(text_path, "rb"), file_name="extracted.txt")

if __name__ == "__main__":
    # Temp-Ordner erstellen
    os.makedirs(AUDIO_TEMP_DIR, exist_ok=True)
    os.makedirs(TEXT_TEMP_DIR, exist_ok=True)
    main()
    clean_temp_files([AUDIO_TEMP_DIR, TEXT_TEMP_DIR])