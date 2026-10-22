import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Meta Spatial AI Assistant Backend")

class GestureRequest(BaseModel):
    gesture_type: str
    target_object_id: str

# Endpoint ini yang akan melayani tampilan UI index.html di http://127.0.0.1:8000
@app.get("/", response_class=HTMLResponse)
async def get_simulation():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>File index.html tidak ditemukan di folder proyek!</h1>"

@app.post("/api/segment-object")
async def segment_with_sam():
    return {
        "status": "success",
        "segmented_object": "document_page_1",
        "confidence": 0.98
    }

@app.post("/api/process-reasoning")
async def process_with_muse(data: GestureRequest):
    return {
        "status": "success",
        "action": "summarize",
        "hud_text": f"Muse Spark processed '{data.gesture_type}' gesture on object '{data.target_object_id}'."
    }