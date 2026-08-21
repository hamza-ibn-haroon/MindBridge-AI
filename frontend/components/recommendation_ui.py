"""
Recommendations UI components.
"""

import streamlit as st
from typing import List, Dict, Any, Optional


def render_recommendations(recommendations: List[str], category: Optional[str] = None):
    """
    Render recommendations as visually distinct cards.
    
    Args:
        recommendations: List of recommendation strings
        category: Optional category label
    """
    if not recommendations:
        st.info("💡 Start a conversation to receive personalized recommendations.")
        return
    
    if category:
        st.markdown(f"### 💡 Recommendations: {category}")
    else:
        st.markdown("### 💡 Recommendations")
    
    for i, recommendation in enumerate(recommendations):
        with st.container():
            st.markdown(f"**{i + 1}.** {recommendation}")
            st.divider()


def render_empty_recommendations_state():
    """Render the state when no recommendations are available."""
    st.info(
        "💡 **No recommendations available yet**\n\n"
        "Start a conversation in the **Chat** page to get personalized recommendations "
        "based on your interactions."
    )