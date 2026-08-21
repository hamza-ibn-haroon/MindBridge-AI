"""
Sidebar component for MindBridge application.
Contains navigation, session controls, and backend status.
"""

import streamlit as st
from typing import Optional
import time

from api.client import APIClient, ConnectionError
from utils.session import SessionManager


def render_sidebar():
    """
    Render the sidebar for the MindBridge application.
    Includes logo, navigation, session controls, and backend status.
    """
    with st.sidebar:
        # Logo and title
        st.markdown("""
        # 🧠 MindBridge
        #### *Your bridge between thoughts and clarity*
        """)
        
        st.divider()
        
        # Navigation is handled by Streamlit's native page navigation
        # We just show the current page
        st.write("**Navigation**")
        
        # Session controls
        st.divider()
        st.write("**Session Controls**")
        
        # Session ID display
        session_id = SessionManager.get_session_id()
        st.caption(f"Session ID: `{session_id[:8]}...`")
        
        # New Conversation button
        if st.button("🔄 New Conversation", use_container_width=True):
            SessionManager.reset_session()
            st.rerun()
        
        # Message count
        message_count = SessionManager.get_message_count()
        st.caption(f"Messages: {message_count}")
        
        st.divider()
        
        # Backend status
        st.write("**Backend Status**")
        _render_backend_status()
        
        st.divider()
        
        # Prototype label
        st.caption("⚠️ MindBridge Prototype v1.0")
        st.caption("Made with ❤️ for Hackathon")


def _render_backend_status():
    """
    Check and display the backend status.
    """
    try:
        client = APIClient()
        health_data = client.health_check()
        status = health_data.get("status", "unknown")
        
        if status == "healthy":
            st.success("🟢 Backend Connected")
            # Show backend URL if development
            import config
            if config.config.is_development():
                st.caption(f"API: {config.config.API_BASE_URL}")
        else:
            st.warning("🟡 Backend Status: Unknown")
    except ConnectionError:
        st.error("🔴 Backend Unavailable")
        st.caption("Please check your connection and try again.")
    except Exception as e:
        st.error(f"🔴 Error: {str(e)}")


def render_backend_status_indicator() -> str:
    """
    Return a status indicator for the backend.
    Used for inline status displays.
    
    Returns:
        str: Status indicator emoji and text
    """
    try:
        client = APIClient()
        health_data = client.health_check()
        if health_data.get("status") == "healthy":
            return "🟢 Online"
        return "🟡 Unknown"
    except:
        return "🔴 Offline"