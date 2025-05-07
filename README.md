# Async API Project using FastAPI

## Features
-  `/upload` — Accepts a document and returns a `job_id`.
-  `/process` — Simulates a 2–3 second processing delay.
-  `/status/{id}` — Returns the status of a job.
-  Fully async using `async def` and `BackgroundTasks`.
-  In-memory job tracking with `uuid`.
---
## Tech Stack
- **Python 3.7+**
- **FastAPI**
- **Uvicorn**




