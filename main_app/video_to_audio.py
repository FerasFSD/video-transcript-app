from moviepy.editor import VideoFileClip
import os

def convert_video_to_audio(video_path, output_ext="mp3"):
    """Konvertiert Video zu Audio"""
    filename, _ = os.path.splitext(video_path)
    audio_path = f"{filename}.{output_ext}"
    
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path