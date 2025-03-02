from setuptools import setup, find_packages

setup(
    name="main_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.33",
        "openai-whisper>=20231117",
        "moviepy>=1.0.3",
        "python-docx>=0.8.11",
        "PyPDF2>=3.0.1",
        "ffmpeg-python>=0.2.0"
    ],
)