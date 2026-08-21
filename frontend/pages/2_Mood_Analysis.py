"""
Mood Analysis page - Analyze mood based on conversation.
"""

import streamlit as st

from components.common import render_header, render_disclaimer, render_error
from components.sidebar import render_sidebar
from components.mood_ui import (
    render_mood_scores,
    render_primary_state,
    render_mood_disclaimer,
    render_empty_mood_state
)
from api.client import APIClient, ConnectionError, APIError
from utils.session import SessionManager


# Page configuration
st.set_page_config(
    page_title="MindBridge - Mood Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session
SessionManager.initialize_session()

# Render sidebar
render_sidebar()


def main():
    """Mood analysis interface."""
    render_header("📊 Mood Analysis", "Understand your emotional patterns")
    
    # Show disclaimer
    render_mood_disclaimer()
    
    st.divider()
    
    # Text input for mood analysis
    st.markdown("### Enter a message to analyze")
    
    text_input = st.text_area(
        "Type a message you want to analyze for mood:",
        placeholder="e.g., I'm feeling really stressed about my upcoming exams...",
        height=100
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        analyze_button = st.button("🔍 Analyze Mood", type="primary", use_container_width=True)
    
    # Analyze button clicked
    if analyze_button and text_input and text_input.strip():
        _analyze_mood(text_input.strip())
    
    st.divider()
    
    # Show current mood analysis if available
    latest_mood = SessionManager.get_latest_mood()
    if latest_mood:
        st.markdown("### 📊 Current Mood Analysis")
        _display_mood_results(latest_mood)
    else:
        st.info("💭 No mood analysis available yet. Use the form above to analyze a message.")
    
    # Display disclaimer
    st.divider()
    render_disclaimer(compact=True)


def _analyze_mood(text: str):
    """Analyze mood for the given text."""
    session_id = SessionManager.get_session_id()
    
    with st.spinner("Analyzing mood..."):
        try:
            client = APIClient()
            result = client.analyze_mood(text, session_id)
            
            # Store in session state
            SessionManager.set_latest_mood(result)
            
            # Rerun to display results
            st.rerun()
            
        except ConnectionError as e:
            render_error(f"Connection Error: {str(e)}", "error")
            st.info("💡 Please check if the MindBridge backend is running and try again.")
        except APIError as e:
            render_error(f"API Error: {str(e)}", "error")
        except Exception as e:
            render_error(f"Unexpected Error: {str(e)}", "error")


def _display_mood_results(result: dict):
    """Display mood analysis results."""
    # Primary state
    primary_state = result.get("primary_state")
    confidence = result.get("confidence")
    if primary_state:
        render_primary_state(primary_state, confidence)
    
    # Scores
    scores = result.get("scores", {})
    if scores:
        st.markdown("### 📊 Mood Dimensions")
        render_mood_scores(scores)
    
    # Additional insights if available
    insights = result.get("insights")
    if insights:
        st.markdown("### 💡 Insights")
        st.info(insights)
    
    # Analyzed text preview
    analyzed_text = result.get("analyzed_text")
    if analyzed_text:
        with st.expander("📝 View analyzed text"):
            st.write(analyzed_text)


if __name__ == "__main__":
    main()