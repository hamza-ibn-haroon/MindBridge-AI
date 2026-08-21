"""
Recommendations page - Display personalized recommendations.
"""

import streamlit as st

from components.common import render_header, render_disclaimer, render_error
from components.sidebar import render_sidebar
from components.recommendation_ui import (
    render_recommendations,
    render_empty_recommendations_state
)
from api.client import APIClient, ConnectionError, APIError
from utils.session import SessionManager


# Page configuration
st.set_page_config(
    page_title="MindBridge - Recommendations",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session
SessionManager.initialize_session()

# Render sidebar
render_sidebar()


def main():
    """Recommendations interface."""
    render_header("🎯 Recommendations", "Personalized guidance for your well-being")
    
    # Check if there's a conversation
    if not SessionManager.has_conversation():
        render_empty_recommendations_state()
        st.divider()
        render_disclaimer(compact=True)
        return
    
    # Refresh button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("🔄 Refresh", type="primary", use_container_width=True):
            st.rerun()
    
    st.divider()
    
    # Get recommendations
    _fetch_and_display_recommendations()
    
    # Display disclaimer
    st.divider()
    render_disclaimer(compact=True)


def _fetch_and_display_recommendations():
    """Fetch and display recommendations from the backend."""
    session_id = SessionManager.get_session_id()
    
    # Show loading state
    with st.spinner("Generating personalized recommendations..."):
        try:
            client = APIClient()
            result = client.get_recommendations(session_id)
            
            # Extract recommendations
            recommendations = result.get("recommendations", [])
            category = result.get("category")
            
            # Display recommendations
            if recommendations:
                render_recommendations(recommendations, category)
            else:
                st.info(
                    "💡 No specific recommendations available yet. "
                    "Continue your conversation to receive personalized guidance."
                )
                
            # Show any additional info
            if "message" in result:
                st.info(result["message"])
            
        except ConnectionError as e:
            render_error(f"Connection Error: {str(e)}", "error")
            st.info("💡 Please check if the MindBridge backend is running and try again.")
        except APIError as e:
            render_error(f"API Error: {str(e)}", "error")
        except Exception as e:
            render_error(f"Unexpected Error: {str(e)}", "error")


if __name__ == "__main__":
    main()