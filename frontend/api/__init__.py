"""
API client module for MindBridge frontend.
Provides a clean interface for communicating with the FastAPI backend.
"""

from .client import APIClient, APIError, ConnectionError

__all__ = ['APIClient', 'APIError', 'ConnectionError']