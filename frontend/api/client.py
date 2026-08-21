"""
API client for MindBridge frontend.
Handles all communication with the FastAPI backend.
"""

import json
import requests
from typing import Optional, Dict, Any, List
from requests.exceptions import RequestException, Timeout, ConnectionError as RequestsConnectionError
import logging

from config import config

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIError(Exception):
    """Custom exception for API-related errors."""
    def __init__(self, message: str, status_code: Optional[int] = None, response_data: Optional[Dict] = None):
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(message)


class ConnectionError(APIError):
    """Exception for connection-related errors."""
    pass


class APIClient:
    """
    Client for communicating with the MindBridge FastAPI backend.
    All API calls go through this class.
    """
    
    def __init__(self, base_url: Optional[str] = None):
        """Initialize the API client with the base URL."""
        self.base_url = base_url or config.API_BASE_URL
        self.timeout = config.REQUEST_TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Request body data (for POST requests)
            params: Query parameters
            
        Returns:
            Dict containing the JSON response
            
        Raises:
            ConnectionError: If connection fails
            APIError: For other API errors
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Making {method} request to {url}")
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                timeout=self.timeout
            )
            
            # Try to parse JSON response
            try:
                response_data = response.json()
            except json.JSONDecodeError:
                response_data = {"error": "Invalid JSON response from server"}
            
            # Check for HTTP errors
            if response.status_code >= 400:
                error_message = response_data.get("detail", response_data.get("error", "Unknown API error"))
                raise APIError(
                    message=error_message,
                    status_code=response.status_code,
                    response_data=response_data
                )
            
            return response_data
            
        except Timeout as e:
            logger.error(f"Request timeout: {e}")
            raise ConnectionError(f"Request timed out after {self.timeout} seconds")
        except RequestsConnectionError as e:
            logger.error(f"Connection error: {e}")
            raise ConnectionError(f"Failed to connect to the backend at {self.base_url}")
        except RequestException as e:
            logger.error(f"Request error: {e}")
            raise ConnectionError(f"Request failed: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise APIError(f"Unexpected error: {str(e)}")
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check if the backend is healthy.
        
        Returns:
            Dict with health status
            
        Raises:
            ConnectionError: If backend is unavailable
        """
        try:
            return self._make_request("GET", config.API_HEALTH)
        except ConnectionError:
            # Re-raise with a clearer message
            raise ConnectionError(f"Backend is unavailable at {self.base_url}")
    
    def send_chat_message(self, message: str, session_id: str) -> Dict[str, Any]:
        """
        Send a chat message to the backend.
        
        Args:
            message: User message text
            session_id: Unique session identifier
            
        Returns:
            Dict containing the chat response
            
        Raises:
            ConnectionError: If backend is unavailable
            APIError: For other API errors
        """
        if not message or not message.strip():
            raise ValueError("Message cannot be empty")
        
        if not session_id:
            raise ValueError("Session ID is required")
        
        data = {
            "message": message.strip(),
            "session_id": session_id
        }
        
        return self._make_request("POST", config.API_CHAT_MESSAGE, data=data)
    
    def analyze_mood(self, text: str, session_id: str) -> Dict[str, Any]:
        """
        Analyze mood from text.
        
        Args:
            text: Text to analyze for mood
            session_id: Unique session identifier
            
        Returns:
            Dict containing mood analysis
            
        Raises:
            ConnectionError: If backend is unavailable
            APIError: For other API errors
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        data = {
            "text": text.strip(),
            "session_id": session_id
        }
        
        return self._make_request("POST", config.API_MOOD_ANALYZE, data=data)
    
    def get_insights(self, session_id: str) -> Dict[str, Any]:
        """
        Get insights for the current session.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            Dict containing insights
            
        Raises:
            ConnectionError: If backend is unavailable
            APIError: For other API errors
        """
        if not session_id:
            raise ValueError("Session ID is required")
        
        data = {"session_id": session_id}
        
        return self._make_request("POST", config.API_INSIGHTS_ANALYZE, data=data)
    
    def get_recommendations(self, session_id: str) -> Dict[str, Any]:
        """
        Get recommendations for the current session.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            Dict containing recommendations
            
        Raises:
            ConnectionError: If backend is unavailable
            APIError: For other API errors
        """
        if not session_id:
            raise ValueError("Session ID is required")
        
        data = {"session_id": session_id}
        
        return self._make_request("POST", config.API_RECOMMENDATIONS_GET, data=data)
    
    def test_connection(self) -> bool:
        """
        Test if the backend is reachable.
        
        Returns:
            bool: True if backend is reachable, False otherwise
        """
        try:
            self.health_check()
            return True
        except (ConnectionError, APIError):
            return False

# Create a global client instance
api_client = APIClient()