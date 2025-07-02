This project demonstrates an asynchronous document processing system built with FastAPI (backend) and Streamlit (frontend). It simulates the real-world scenario of uploading documents, processing them asynchronously in the background, and tracking the processing status in real-time via a user-friendly interface.

# Features
Asynchronous Processing:
Handles document uploads and simulates time-consuming processing without blocking the server.
Job Tracking:
Each upload returns a unique Job ID, which can be used to check the current status (uploaded, processed).
Interactive Frontend:
Streamlit interface for submitting documents and viewing live updates.
Simple In-Memory Storage:
Stores job data and status in memory for demonstration purposes.

# Technologies Used
Backend: FastAPI (Python)
Frontend: Streamlit (Python)
Deployment: Render (backend), Streamlit Cloud (frontend)




