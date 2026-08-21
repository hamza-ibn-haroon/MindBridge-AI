"""
Session management utilities for Streamlit session state.
"""

import uuid
from typing import List, Dict, Any, Optional
import streamlit as st

from config import config


class SessionManager:
    """
    Manages Streamlit session state for the MindBridge application.
    All session-related operations go through this class.
    """
    
    @staticmethod
    def initialize_session():
        """
        Initialize the session state with default values.
        Should be called once per user session.
        """
        if "initialized" not in st.session_state:
            st.session_state.initialized = True
            st.session_state.session_id = str(uuid.uuid4())
            st.session_state.messages = []
            st.session_state.latest_response = None
            st.session_state.latest_intent = None
            st.session_state.latest_confidence = None
            st.session_state.latest_entities = None
            st.session_state.latest_recommendations = []
            st.session_state.latest_safety_level = None
            st.session_state.latest_mood = None
            st.session_state.conversation_count = 0
    
    @staticmethod
    def get_session_id() -> str:
        """Get the current session ID."""
        SessionManager.initialize_session()
        return st.session_state.session_id
    
    @staticmethod
    def reset_session():
        """
        Reset the session with a new session ID.
        Clears all conversation history and analysis.
        """
        SessionManager.initialize_session()
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.session_state.latest_response = None
        st.session_state.latest_intent = None
        st.session_state.latest_confidence = None
        st.session_state.latest_entities = None
        st.session_state.latest_recommendations = []
        st.session_state.latest_safety_level = None
        st.session_state.latest_mood = None
        st.session_state.conversation_count = 0
    
    @staticmethod
    def add_message(role: str, content: str, metadata: Optional[Dict] = None):
        """
        Add a message to the conversation history.
        
        Args:
            role: "user" or "assistant"
            content: Message content
            metadata: Optional metadata about the message
        """
        SessionManager.initialize_session()
        
        message = {
            "role": role,
            "content": content,
            "metadata": metadata or {}
        }
        
        st.session_state.messages.append(message)
        
        # Limit messages to prevent excessive memory usage
        if len(st.session_state.messages) > config.MAX_HISTORY_MESSAGES:
            st.session_state.messages = st.session_state.messages[-config.MAX_HISTORY_MESSAGES:]
        
        if role == "user":
            st.session_state.conversation_count += 1
    
    @staticmethod
    def get_messages() -> List[Dict]:
        """Get all messages in the conversation history."""
        SessionManager.initialize_session()
        return st.session_state.messages
    
    @staticmethod
    def get_last_message() -> Optional[Dict]:
        """Get the last message in the conversation."""
        SessionManager.initialize_session()
        if st.session_state.messages:
            return st.session_state.messages[-1]
        return None
    
    @staticmethod
    def get_conversation_count() -> int:
        """Get the total number of user messages in the conversation."""
        SessionManager.initialize_session()
        return st.session_state.conversation_count
    
    @staticmethod
    def set_latest_response(response_data: Dict):
        """
        Set the latest response data from the backend.
        
        Args:
            response_data: The response from the chat API
        """
        SessionManager.initialize_session()
        st.session_state.latest_response = response_data.get("response")
        st.session_state.latest_intent = response_data.get("intent")
        st.session_state.latest_confidence = response_data.get("confidence")
        st.session_state.latest_entities = response_data.get("entities", {})
        st.session_state.latest_recommendations = response_data.get("recommendations", [])
        st.session_state.latest_safety_level = response_data.get("safety_level", "normal")
    
    @staticmethod
    def get_latest_response() -> Dict[str, Any]:
        """Get the latest response data."""
        SessionManager.initialize_session()
        return {
            "response": st.session_state.latest_response,
            "intent": st.session_state.latest_intent,
            "confidence": st.session_state.latest_confidence,
            "entities": st.session_state.latest_entities,
            "recommendations": st.session_state.latest_recommendations,
            "safety_level": st.session_state.latest_safety_level
        }
    
    @staticmethod
    def set_latest_mood(mood_data: Dict):
        """Set the latest mood analysis data."""
        SessionManager.initialize_session()
        st.session_state.latest_mood = mood_data
    
    @staticmethod
    def get_latest_mood() -> Optional[Dict]:
        """Get the latest mood analysis data."""
        SessionManager.initialize_session()
        return st.session_state.latest_mood
    
    @staticmethod
    def has_conversation() -> bool:
        """Check if there is any conversation history."""
        SessionManager.initialize_session()
        return len(st.session_state.messages) > 0
    
    @staticmethod
    def get_message_count() -> int:
        """Get the total number of messages in the conversation."""
        SessionManager.initialize_session()
        return len(st.session_state.messages)