from setuptools import setup, find_packages

setup(
    name="video_transcript_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.33.0",
        "whisper==20231117",
        # alle anderen requirements
    ],
)