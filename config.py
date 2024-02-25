import os


class Config:
    TESSERACT_CMD = os.getenv('TESSERACT_CMD',default=r"C:\Program Files\Tesseract-OCR\tesseract.exe")
