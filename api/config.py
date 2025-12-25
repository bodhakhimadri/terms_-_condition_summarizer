import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Terms & Conditions Summarizer API"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"

settings = Settings()