"""
Chat UI components for the MindBridge chat interface.
"""

import streamlit as st
from typing import List, Dict, Any, Optional
import time

from utils.formatting import (
    format_intent_name,
    format_confidence,
    format_safety_label,
    format_entities,
    get_confidence_color
)
from utils.session import SessionManager


def render_chat_message(message: Dict[str, Any]):
    """
    Render a single chat message.
    
    Args:
        message: Message dict with 'role' and 'content'
    """
    role = message.get("role", "user")
    content = message.get("content", "")
    
    if role == "user":
        with st.chat_message("user"):
            st.write(content)
    else:
        with st.chat_message("assistant"):
            st.write(content)
            
            # If this is a recent assistant message with metadata
            metadata = message.get("metadata", {})
            if metadata and metadata.get("show_explanation", False):
                render_chat_explanation(metadata)


def render_chat_history(messages: List[Dict[str, Any]]):
    """
    Render the entire chat history.
    
    Args:
        messages: List of message dicts
    """
    for message in messages:
        render_chat_message(message)


def render_chat_explanation(metadata: Dict[str, Any]):
    """
    Render an expandable explanation section for a chat response.
    
    Args:
        metadata: Metadata containing intent, confidence, entities, etc.
    """
    with st.expander("💡 Why MindBridge responded this way"):
        intent = metadata.get("intent")
        confidence = metadata.get("confidence")
        entities = metadata.get("entities", {})
        safety_level = metadata.get("safety_level", "normal")
        matched_keywords = metadata.get("matched_keywords", [])
        matched_phrases = metadata.get("matched_phrases", [])
        
        cols = st.columns(2)
        
        with cols[0]:
            st.write("**Detected Intent**")
            if intent:
                st.markdown(f"**{format_intent_name(intent)}**")
            else:
                st.write("Unknown")
            
            st.write("**Confidence**")
            if confidence is not None:
                color = get_confidence_color(confidence)
                st.markdown(f"**<span style='color:{color};'>{format_confidence(confidence)}</span>**", unsafe_allow_html=True)
            else:
                st.write("N/A")
        
        with cols[1]:
            st.write("**Safety Level**")
            st.write(f"**{format_safety_label(safety_level)}**")
            
            st.write("**Detected Topics**")
            entities_str = format_entities(entities)
            if entities_str:
                st.write(entities_str)
            else:
                st.write("No topics detected")
        
        if matched_keywords or matched_phrases:
            st.write("**Matched Signals**")
            if matched_keywords:
                st.write(f"Keywords: {', '.join(matched_keywords)}")
            if matched_phrases:
                st.write(f"Phrases: {', '.join(matched_phrases)}")


def render_quick_actions():
    """
    Render quick action buttons for common messages.
    """
    st.write("**Quick Actions**")
    
    quick_actions = [
        ("😟 I'm feeling stressed", "I'm feeling stressed and overwhelmed."),
        ("😰 I'm anxious", "I'm feeling anxious and worried."),
        ("📚 I'm struggling with studies", "I'm struggling with my studies and feel lost."),
        ("😔 I'm feeling lonely", "I'm feeling lonely and isolated."),
        ("💪 I need motivation", "I need some motivation to get through this.")
    ]
    
    # Create 5 columns for the buttons
    cols = st.columns(5)
    
    for i, (label, message) in enumerate(quick_actions):
        with cols[i]:
            if st.button(label, key=f"quick_action_{i}", use_container_width=True):
                # Send the quick action message
                session_id = SessionManager.get_session_id()
                if session_id:
                    # Add user message to history
                    SessionManager.add_message("user", message)
                    # The actual sending will be handled in the page
                    # We pass the message through session state
                    st.session_state.quick_action_message = message
                    st.rerun()


def render_safety_response(response_data: Dict[str, Any]):
    """
    Render a response with safety considerations.
    
    Args:
        response_data: The response data from the API
    """
    safety_level = response_data.get("safety_level", "normal")
    response_text = response_data.get("response", "")
    
    if safety_level == "high_risk":
        st.error("🚨 **High Risk Detected**")
        st.warning(response_text)
        st.error("⚠️ **Please consider reaching out to a mental health professional immediately.**")
        # Add a help line button
        if st.button("📞 Show Support Resources", key="show_resources"):
            st.info(
                "If you need immediate support:\n\n"
                "- 📞 Call a mental health professional\n"
                "- 📞 Contact a trusted friend or family member\n"
                "- 🏥 Visit your nearest emergency room\n\n"
                "*Please reach out for help. You are not alone.*"
            )
    elif safety_level == "concern":
        st.warning("⚠️ **Moderate Concern**")
        st.info(response_text)
        st.info("💡 It may be helpful to talk to a trusted person or professional about these feelings.")
    else:
        st.success("💬 MindBridge")
        st.write(response_text)
    
    # Store the response in session state
    SessionManager.set_latest_response(response_data)


def render_typing_indicator():
    """Render a typing indicator for the assistant."""
    with st.chat_message("assistant"):
        st.write("⏳ MindBridge is thinking...")