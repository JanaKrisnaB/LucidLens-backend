from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
import shutil
from utils import ocr_text
from summarizer import summarize_text
from explainer import explain_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="🖼️ Image to Text Summarizer & Explainer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Allow CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/process")
async def process_image(
    file: UploadFile = File(...),
    mode: str = Form(...)
):
    # Save uploaded image
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR
    text, count = ocr_text(file_path)

    if count < 5:
        return JSONResponse(
            {"error": "Text too short to process.", "text": text},
            status_code=400
        )

    if mode == "text":
        result = text
    elif mode == "summary":
        result = summarize_text(text, count)
    elif mode == "explain":
        result = explain_text(text)
    else:
        return JSONResponse({"error": "Invalid mode selected."}, status_code=400)

    return JSONResponse({"result": result})
