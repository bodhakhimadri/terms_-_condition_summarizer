from fastapi import APIRouter, HTTPException
from api.schemas.summarize_schema import SummarizeRequest, SummarizeResponse
from core.pipeline import run_pipeline

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    try:
        result = run_pipeline(
            text=request.text,
            url=request.url,
            summary_type=request.summary_type
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
