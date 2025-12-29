from fastapi import APIRouter, HTTPException
from api.schemas.summarize_schema import SummarizeRequest, SummarizeResponse
from core.pipeline import run_pipeline

router = APIRouter(prefix="/api", tags=["Summarization"])


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    """
    Accepts text or URL and returns summarized output
    """
    try:
        result = run_pipeline(
            text=request.text,
            url=request.url,
            summary_type=request.summary_type
        )
        return result

    except ValueError as ve:
        # Input / validation related errors
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        # Internal server errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

