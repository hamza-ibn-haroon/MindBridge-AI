"""Configuration for MindBridge."""

from typing import List
import os

class Config:
    """Application configuration."""
    
    APP_TITLE = "MindBridge API"
    APP_DESCRIPTION = "Intent-based conversational support system"
    APP_VERSION = "1.0.0"
    
    # CORS
    ALLOWED_ORIGINS = ["*"]  # For development only
    ALLOWED_METHODS = ["*"]
    ALLOWED_HEADERS = ["*"]
    
    # Limits
    MAX_MESSAGE_LENGTH = 2000
    MAX_SESSION_HISTORY = 10
    
    # Session
    SESSION_EXPIRY_SECONDS = 3600
    
    @classmethod
    def get_allowed_origins(cls) -> List[str]:
        """Get allowed origins for CORS."""
        # In production, restrict to specific origins
        if os.getenv("ENVIRONMENT") == "production":
            return [
                "https://your-streamlit-app.com",
            ]
        return cls.ALLOWED_ORIGINS