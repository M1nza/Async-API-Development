from pydantic import BaseModel
from typing import Optional, Dict

class Document(BaseModel):
    id: str
    type: str
    content: Optional[Dict] = {}

class JobStatus:
    def __init__(self, status: str, data: Document):
        self.status = status
        self.data = data

