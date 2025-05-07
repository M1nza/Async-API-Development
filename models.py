from pydantic import BaseModel

class Document(BaseModel):
    id: str
    type: str  # e.g., "invoice" or "contract"
    content: dict
