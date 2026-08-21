"""
Insights UI components.
"""

import streamlit as st
from typing import Dict, Any, List, Optional

from utils.formatting import format_intent_name


def render_insights(insights: Dict[str, Any]):
    """
    Render insights in a clean, card-like format.
    
    Args:
        insights: Insights data from the API
    """
    if not insights or not insights.get("has_conversation", False):
        st.info("💭 Start a conversation to generate insights.")
        return
    
    # Current focus
    current_focus = insights.get("current_focus")
    if current_focus:
        st.markdown("### 🎯 Current Focus")
        st.success(f"**{format_intent_name(current_focus)}**")
    
    # Main trigger
    main_trigger = insights.get("main_trigger")
    if main_trigger:
        st.markdown("### 🔍 Main Trigger")
        st.info(f"**{main_trigger.title()}**")
    
    # Dominant topic
    dominant_topic = insights.get("dominant_topic")
    if dominant_topic:
        st.markdown("### 📚 Dominant Topic")
        st.write(f"Your conversations are primarily about **{dominant_topic.lower()}**.")
    
    # Recent pattern
    recent_pattern = insights.get("recent_pattern")
    if recent_pattern:
        st.markdown("### 📊 Recent Pattern")
        st.write(recent_pattern)
    
    # Suggested action
    suggested_action = insights.get("suggested_action")
    if suggested_action:
        st.markdown("### 💡 Suggested Action")
        st.info(f"**{suggested_action}**")
    
    # Conversation stats
    conversation_count = insights.get("conversation_count", 0)
    if conversation_count > 0:
        st.markdown("### 📈 Conversation Stats")
        st.metric("Total Messages", f"{conversation_count}")


def render_empty_insights_state():
    """Render the state when no insights are available."""
    st.info(
        "💭 **No insights available yet**\n\n"
        "Start a conversation in the **Chat** page to generate insights about your interactions."
    )