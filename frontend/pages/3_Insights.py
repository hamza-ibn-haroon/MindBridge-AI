"""
Insights page - Display conversation insights.
"""

import streamlit as st

from components.common import render_header, render_disclaimer, render_error, render_loading
from components.sidebar import render_sidebar
from components.insight_ui import render_insights, render_empty_insights_state
from api.client import APIClient, ConnectionError, APIError
from utils.session import SessionManager


# Page configuration
st.set_page_config(
    page_title="MindBridge - Insights",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session
SessionManager.initialize_session()

# Render sidebar
render_sidebar()


def main():
    """Insights interface."""
    render_header("💡 Insights", "Discover patterns and insights from your conversations")
    
    # Check if there's a conversation
    if not SessionManager.has_conversation():
        render_empty_insights_state()
        st.divider()
        render_disclaimer(compact=True)
        return
    
    # Refresh button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("🔄 Refresh", type="primary", use_container_width=True):
            st.rerun()
    
    st.divider()
    
    # Get insights
    _fetch_and_display_insights()
    
    # Display disclaimer
    st.divider()
    render_disclaimer(compact=True)


def _fetch_and_display_insights():
    """Fetch and display insights from the backend."""
    session_id = SessionManager.get_session_id()
    
    # Show loading state
    with st.spinner("Analyzing conversation patterns..."):
        try:
            client = APIClient()
            insights = client.get_insights(session_id)
            
            # Display insights
            render_insights(insights)
            
        except ConnectionError as e:
            render_error(f"Connection Error: {str(e)}", "error")
            st.info("💡 Please check if the MindBridge backend is running and try again.")
        except APIError as e:
            render_error(f"API Error: {str(e)}", "error")
        except Exception as e:
            render_error(f"Unexpected Error: {str(e)}", "error")


if __name__ == "__main__":
    main()