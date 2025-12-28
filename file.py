from fastapi import FastAPI, UploadFile, File
import requests
from dotenv import load_dotenv
import os

api = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("model")
app = FastAPI()

@app.post("/upload")
async def file_upload(file: UploadFile=File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        header = {"Authorization":f"Bearer {api}","Content-Type" : "application/json"},
        json = {
            "model" : model,
            "messages":[{"role":"system","content":"summarize the text"},
                        {"role":"user","content":text}]
        }
    ) 

    return response.json()

import pdfplumber

@app.post("/upload-pdf")
async def upload_pdf(file:UploadFile = File(...)):
    with pdfplumber.open(file.file) as f:
        text = ""
        for page in f.pages:
            text+=page.extract_text()

    return {"extracted_text":text[:500]}