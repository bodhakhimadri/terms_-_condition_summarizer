from fastapi import FastAPI
from api.config import settings
from api.routes.health import router as health_router
from api.routes.summarize import router as summarize_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# Register routes
app.include_router(health_router, tags=["Health"])
app.include_router(summarize_router, tags=["Summarize"])

@app.get("/")
def root():
    return {
        "message": "Terms & Conditions Summarizer API is running"
    }
