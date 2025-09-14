import pytesseract
from PIL import Image

def ocr_text(img_path):
    """Extracts text from image using Tesseract and counts words."""
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)

    # Count words
    words = text.split()
    count = len(words)

    return text.strip(), count
