from fastapi import FastAPI, BackgroundTasks
from models import Document, JobStatus
from uuid import uuid4
import asyncio

app = FastAPI()
jobs = {}

@app.post("/upload")
async def upload_document(doc: Document, background_tasks: BackgroundTasks):
    job_id = str(uuid4())
    jobs[job_id] = JobStatus(status="uploaded", data=doc)
    background_tasks.add_task(process_document, job_id)
    return {"message": "Document received", "job_id": job_id}

@app.get("/process")
async def simulate_processing():
    await asyncio.sleep(2)
    return {"message": "Simulated async processing complete"}

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    if job_id not in jobs:
        return {"error": "Job not found"}
    return {"job_id": job_id, "status": jobs[job_id].status}

async def process_document(job_id: str):
    await asyncio.sleep(3)
    jobs[job_id].status = "processed"
