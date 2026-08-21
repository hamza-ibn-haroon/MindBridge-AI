"""
Chat page - Main conversation interface for MindBridge.
"""

import streamlit as st
import time

from components.common import render_header, render_disclaimer
from components.sidebar import render_sidebar
from components.chat_ui import (
    render_chat_history,
    render_chat_message,
    render_quick_actions,
    render_safety_response,
    render_typing_indicator
)
from api.client import APIClient, ConnectionError, APIError
from utils.session import SessionManager
from utils.formatting import format_intent_name, format_confidence


# Page configuration
st.set_page_config(
    page_title="MindBridge - Chat",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session
SessionManager.initialize_session()

# Render sidebar
render_sidebar()


def main():
    """Main chat interface."""
    render_header("💬 Chat", "Have a supportive conversation with MindBridge")
    
    # Initialize session state for quick actions
    if "quick_action_message" not in st.session_state:
        st.session_state.quick_action_message = None
    
    # Check for quick action
    if st.session_state.quick_action_message:
        message = st.session_state.quick_action_message
        st.session_state.quick_action_message = None
        _process_message(message)
    
    # Render chat history
    messages = SessionManager.get_messages()
    if messages:
        render_chat_history(messages)
    else:
        st.info("💭 Start a conversation by typing a message below.")
    
    # Quick actions
    st.divider()
    render_quick_actions()
    st.divider()
    
    # Chat input
    prompt = st.chat_input("How are you feeling today?")
    
    if prompt:
        _process_message(prompt)
    
    # Display disclaimer
    st.divider()
    render_disclaimer(compact=True)


def _process_message(message: str):
    """Process a user message and get a response from the backend."""
    # Add user message to history
    SessionManager.add_message("user", message)
    
    # Get session ID
    session_id = SessionManager.get_session_id()
    
    # Show typing indicator
    render_typing_indicator()
    
    # Send to backend
    try:
        client = APIClient()
        response_data = client.send_chat_message(message, session_id)
        
        # Extract response data
        response_text = response_data.get("response", "")
        safety_level = response_data.get("safety_level", "normal")
        intent = response_data.get("intent")
        confidence = response_data.get("confidence")
        entities = response_data.get("entities", {})
        matched_keywords = response_data.get("matched_keywords", [])
        matched_phrases = response_data.get("matched_phrases", [])
        recommendations = response_data.get("recommendations", [])
        
        # Update session state with response data
        SessionManager.set_latest_response(response_data)
        
        # Add assistant message to history with metadata
        metadata = {
            "intent": intent,
            "confidence": confidence,
            "entities": entities,
            "safety_level": safety_level,
            "matched_keywords": matched_keywords,
            "matched_phrases": matched_phrases,
            "show_explanation": True
        }
        SessionManager.add_message("assistant", response_text, metadata)
        
        # Store recommendations
        if recommendations:
            st.session_state.latest_recommendations = recommendations
        
        # Rerun to display the response
        st.rerun()
        
    except ConnectionError as e:
        st.error(f"❌ Connection Error: {str(e)}")
        st.info("💡 Please check if the MindBridge backend is running and try again.")
    except APIError as e:
        st.error(f"❌ API Error: {str(e)}")
        if hasattr(e, 'status_code') and e.status_code == 400:
            st.info("💡 Please try rephrasing your message.")
    except ValueError as e:
        st.error(f"❌ Validation Error: {str(e)}")
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
        st.info("💡 Please try again later.")


if __name__ == "__main__":
    main()