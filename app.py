import streamlit as st
import requests
import time

# Change this to your actual deployed backend API
API_BASE = "https://async-api-backend.onrender.com"

st.title("📄 Async Document Processor (Frontend)")

with st.form("upload_form"):
    doc_type = st.selectbox("Document Type", ["PDF", "Text", "Image"])
    content = st.text_area("Document Content (JSON or text)")
    submitted = st.form_submit_button("Submit Document")

if submitted:
    with st.spinner("Uploading..."):
        response = requests.post(f"{API_BASE}/upload", json={
            "id": "user-doc",
            "type": doc_type,
            "content": {"text": content}
        })

    if response.status_code == 200:
        job_id = response.json()["job_id"]
        st.success(f"Document uploaded! Job ID: {job_id}")

        status = "uploaded"
        with st.spinner("Processing..."):
            while status != "processed":
                res = requests.get(f"{API_BASE}/status/{job_id}")
                status = res.json().get("status", "unknown")
                st.info(f"Current Status: {status}")
                time.sleep(1)
            st.success("✅ Processing complete!")
    else:
        st.error("Failed to upload document.")

