from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    query: str
    user_id: Optional[str] = None
    image: Optional[bytes] = None  # For image bytes upload

class ResponseModel(BaseModel):
    answer: str
    context_used: Optional[list] = None

