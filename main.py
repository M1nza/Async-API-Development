from fastapi import FastAPI, BackgroundTasks, HTTPException
from models import Document
import asyncio
import uuid

app = FastAPI()

# In-memory database for simplicity
fake_db = {}

@app.post("/upload")
async def upload_doc(doc: Document, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    fake_db[job_id] = {"status": "uploaded", "data": doc}
    background_tasks.add_task(process_doc, job_id)
    return {"message": "Document received", "job_id": job_id}

async def process_doc(job_id: str):
    await asyncio.sleep(2.5)  # simulate processing delay
    if job_id in fake_db:
        fake_db[job_id]["status"] = "processed"

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    if job_id not in fake_db:
        raise HTTPException(status_code=404, detail="Job ID not found")
    return {"job_id": job_id, "status": fake_db[job_id]["status"]}

@app.get("/process")
async def simulate_processing():
    await asyncio.sleep(3)  # simulate delay
    return {"message": "Simulated async processing complete"}
