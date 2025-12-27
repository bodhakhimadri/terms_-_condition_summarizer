"""
model_loader.py

This file is responsible for loading and managing the LLM model.
In this project, we use an API-based or mock LLM instead of training a model.
"""

import os


class ModelLoader:
    def __init__(self):
        """
        Initialize model configuration.
        This project does NOT train a model.
        We only prepare configuration for using an LLM.
        """
        self.model_name = os.getenv("MODEL_NAME", "mock-llm")
        self.api_key = os.getenv("API_KEY", None)

    def load_model(self):
        """
        Load or initialize the model.

        For academic purposes:
        - Returns a mock model object
        - Can be extended later to OpenAI / HuggingFace
        """
        if self.api_key:
            return {
                "model": self.model_name,
                "status": "API model ready"
            }
        else:
            return {
                "model": "mock-model",
                "status": "Running in mock mode (no API key)"
            }


# Singleton loader (optional)
model_loader = ModelLoader()


def get_model():
    """
    Used by summarizer or pipeline to get model configuration
    """
    return model_loader.load_model()
