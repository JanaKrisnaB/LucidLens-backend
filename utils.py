import cv2
import numpy as np
from PIL import Image
import io
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def preprocess_image(img_path):
    """
    Preprocess the image using OpenCV before OCR.
    Steps: grayscale → denoise → threshold → resize
    """
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding (binary image)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    scale = 2
    resized = cv2.resize(thresh, (img.shape[1]*scale, img.shape[0]*scale))

    temp_path = "processed.png"
    cv2.imwrite(temp_path, resized)

    return temp_path


def ocr_text(img_path):
    """
    Performs OCR using Gemini Vision API after preprocessing.
    """
    processed_path = preprocess_image(img_path)

    # Opening image as binary
    with open(processed_path, "rb") as f:
        img_bytes = f.read()

    response = model.generate_content(
        [
            {"mime_type": "image/png", "data": img_bytes},
            "Extract all readable text from this image."
        ]
    )

    text = response.text.strip()
    count = len(text.split())

    return text, count

