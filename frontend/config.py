"""
Configuration module for MindBridge frontend.
All configuration values are loaded from environment variables with fallbacks.
"""

import os
from typing import Optional

class Config:
    """Central configuration class for the MindBridge frontend."""
    
    # Backend API URL - configurable via environment variable
    # For production: MINDBRIDGE_API_URL=https://mindbridge-api.onrender.com
    # For local: MINDBRIDGE_API_URL=http://127.0.0.1:8000
    API_BASE_URL: str = os.getenv(
        "MINDBRIDGE_API_URL",
        "http://127.0.0.1:8000"
    )
    
    # API endpoints
    API_HEALTH: str = "/api/health/"
    API_CHAT_MESSAGE: str = "/api/chat/message"
    API_MOOD_ANALYZE: str = "/api/mood/analyze"
    API_INSIGHTS_ANALYZE: str = "/api/insights/analyze"
    API_RECOMMENDATIONS_GET: str = "/api/recommendations/get"
    
    # Timeout settings (in seconds)
    REQUEST_TIMEOUT: int = 30
    
    # Session settings
    MAX_HISTORY_MESSAGES: int = 100
    
    @classmethod
    def get_full_url(cls, endpoint: str) -> str:
        """Return full URL for an API endpoint."""
        return f"{cls.API_BASE_URL}{endpoint}"
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if running in development mode."""
        return "127.0.0.1" in cls.API_BASE_URL or "localhost" in cls.API_BASE_URL

# Global config instance
config = Config()