"""
Main application entry point for MindBridge.
Landing page with branding, navigation, and call-to-action.
"""

import streamlit as st

from components.common import render_header, render_disclaimer, render_page_title
from components.sidebar import render_sidebar
from utils.session import SessionManager


# Page configuration
st.set_page_config(
    page_title="MindBridge - Your Bridge Between Thoughts and Clarity",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session
SessionManager.initialize_session()

# Render sidebar
render_sidebar()


def main():
    """Main function for the home page."""
    # Header
    render_page_title("🧠 MindBridge", None)
    st.markdown("#### *Your bridge between thoughts and clarity.*")
    
    st.divider()
    
    # Hero section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Welcome to MindBridge
        
        MindBridge is an intent-based conversational support application that helps you 
        understand and navigate your thoughts and feelings through supportive conversation.
        
        **How it works:**
        1. 💬 Start a conversation in the **Chat** page
        2. 🔍 MindBridge analyzes your messages for intent and context
        3. 💡 Get insights and personalized recommendations
        4. 📊 Track your mood and patterns over time
        
        MindBridge provides a safe, judgment-free space to explore your thoughts.
        """)
        
        # Call to action
        st.markdown("### Ready to start?")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("💬 Start Conversation", use_container_width=True, type="primary"):
                st.switch_page("pages/1_Chat.py")
        with col_btn2:
            if st.button("📖 Learn More", use_container_width=True):
                st.switch_page("pages/5_About.py")
    
    with col2:
        st.markdown("""
        ### Quick Links
        - 💬 [Chat](Chat)
        - 📊 [Mood Analysis](Mood_Analysis)
        - 💡 [Insights](Insights)
        - 🎯 [Recommendations](Recommendations)
        - ℹ️ [About](About)
        """)
    
    st.divider()
    
    # Features section
    st.markdown("### 🚀 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **💬 Intent-Based Chat**
        - Natural conversation interface
        - Real-time intent detection
        - Explainable responses
        """)
    
    with col2:
        st.markdown("""
        **📊 Mood Analysis**
        - Rule-based emotional estimation
        - Visual mood tracking
        - Pattern recognition
        """)
    
    with col3:
        st.markdown("""
        **💡 Insights & Recommendations**
        - Personalized insights
        - Actionable recommendations
        - Progress tracking
        """)
    
    st.divider()
    
    # Privacy and disclaimer
    st.markdown("### 🔒 Privacy & Data")
    st.markdown(
        "Your conversation data is **temporary and not stored** anywhere. "
        "All processing happens in real-time and data is not persisted."
    )
    
    # Disclaimer
    render_disclaimer(compact=False)


if __name__ == "__main__":
    main()