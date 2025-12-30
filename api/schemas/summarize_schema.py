from typing import Optional, List
from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None
    summary_type: Optional[str] = "simple"


class SummarizeResponse(BaseModel):
    summary: str
    key_points: List[str]
    risk_notes: List[str]
