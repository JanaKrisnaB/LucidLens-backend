import easyocr

# load once (important, otherwise memory heavy)
reader = easyocr.Reader(['en'])

def ocr_text(file_path: str):
    """
    Extract text and word count using EasyOCR.
    """
    results = reader.readtext(file_path, detail=0)  # only text
    text = " ".join(results)
    word_count = len(text.split())
    return text, word_count
