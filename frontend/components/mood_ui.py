"""
Mood analysis UI components.
"""

import streamlit as st
from typing import Dict, Any, Optional, List, Tuple

from utils.formatting import format_score, format_intent_name


def render_mood_scores(scores: Dict[str, float]):
    """
    Render mood scores as progress bars.
    
    Args:
        scores: Dictionary mapping mood dimensions to scores (0-100)
    """
    if not scores:
        st.info("No mood data available. Start a conversation to analyze your mood.")
        return
    
    # Sort scores by value (highest first)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    for label, value in sorted_scores:
        # Format label
        display_label = format_intent_name(label)
        # Create a progress bar with label
        st.write(f"**{display_label}**")
        st.progress(value / 100)
        st.caption(f"{value:.0f}%")


def render_primary_state(primary_state: str, score: Optional[float] = None):
    """
    Render the primary mood state with emphasis.
    
    Args:
        primary_state: The primary detected mood/state
        score: Optional confidence score
    """
    if not primary_state:
        st.info("No primary state detected.")
        return
    
    display_name = format_intent_name(primary_state)
    
    st.markdown("### 🎯 Primary State")
    
    if score is not None:
        st.markdown(f"**{display_name}**")
        st.metric("Confidence", f"{score:.0f}%")
    else:
        st.markdown(f"**{display_name}**")


def render_mood_disclaimer():
    """Render the mood analysis disclaimer."""
    st.info(
        "**📋 Important Note**\n\n"
        "This is a **rule-based conversational estimate** and "
        "**not a clinical or medical assessment.**\n\n"
        "Mood analysis is based on keywords and patterns in your messages, "
        "and should not be used for diagnosis or treatment decisions."
    )


def render_mood_analysis_result(result: Dict[str, Any]):
    """
    Render complete mood analysis results.
    
    Args:
        result: Complete mood analysis result from the API
    """
    if not result:
        st.info("No mood analysis available.")
        return
    
    # Display primary state
    primary_state = result.get("primary_state")
    confidence = result.get("confidence")
    if primary_state:
        render_primary_state(primary_state, confidence)
    
    # Display all scores
    scores = result.get("scores", {})
    if scores:
        st.markdown("### 📊 Mood Dimensions")
        render_mood_scores(scores)
    
    # Display any additional insights
    if "insights" in result:
        st.markdown("### 💡 Insights")
        st.write(result["insights"])
    
    # Display disclaimer
    st.divider()
    render_mood_disclaimer()


def render_empty_mood_state():
    """Render the state when no mood analysis is available."""
    st.info(
        "😌 **No mood analysis available yet**\n\n"
        "Start a conversation in the **Chat** page or type a message above to analyze your mood."
    )