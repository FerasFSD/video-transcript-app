from PyPDF2 import PdfReader
from docx import Document
import os

def extract_text_from_file(file_path):
    """Extrahiert Text aus verschiedenen Dateiformaten"""
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.pdf':
        return extract_from_pdf(file_path)
    elif ext == '.docx':
        return extract_from_docx(file_path)
    elif ext in ('.txt', '.md'):
        return extract_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def extract_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = '\n'.join([page.extract_text() for page in reader.pages])
    return text

def extract_from_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_from_txt(file_path):
    with open(file_path, 'r') as f:
        return f.read()