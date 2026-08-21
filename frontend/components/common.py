"""
Common UI components used across multiple pages.
"""

import streamlit as st
from typing import Optional, Dict, Any


def render_header(title: str, subtitle: Optional[str] = None):
    """
    Render a page header with title and optional subtitle.
    
    Args:
        title: Page title
        subtitle: Optional subtitle text
    """
    st.markdown(f"# {title}")
    if subtitle:
        st.markdown(f"*{subtitle}*")
    st.divider()


def render_page_title(title: str, emoji: Optional[str] = None):
    """
    Render a page title with optional emoji.
    
    Args:
        title: Page title
        emoji: Optional emoji to display
    """
    if emoji:
        st.markdown(f"# {emoji} {title}")
    else:
        st.markdown(f"# {title}")


def render_disclaimer(compact: bool = False):
    """
    Render the MindBridge disclaimer.
    
    Args:
        compact: Whether to show a compact version
    """
    if compact:
        st.caption(
            "⚠️ *MindBridge is a prototype for supportive conversations "
            "and is not a substitute for professional medical or mental-health care.*"
        )
    else:
        st.info(
            "**⚠️ Important Disclaimer**\n\n"
            "MindBridge is a prototype for supportive conversations and "
            "**is not a substitute for professional medical or mental-health care.**\n\n"
            "If you are in crisis or experiencing thoughts of self-harm, "
            "please contact a mental health professional or emergency services immediately."
        )


def render_error(error_message: str, error_type: str = "error"):
    """
    Render an error message with appropriate styling.
    
    Args:
        error_message: The error message to display
        error_type: "error", "warning", or "info"
    """
    if error_type == "error":
        st.error(f"❌ {error_message}")
    elif error_type == "warning":
        st.warning(f"⚠️ {error_message}")
    else:
        st.info(f"ℹ️ {error_message}")


def render_loading(message: str = "Loading..."):
    """
    Render a loading indicator.
    
    Args:
        message: Loading message to display
    """
    with st.spinner(message):
        # This just displays the spinner
        pass


def render_safety_warning(safety_level: str, response: str):
    """
    Render a safety warning based on safety level.
    
    Args:
        safety_level: "normal", "concern", or "high_risk"
        response: The response text from the backend
    """
    if safety_level == "high_risk":
        st.error("🚨 **High Risk Detected**")
        st.warning(response)
        st.warning("⚠️ **Please consider reaching out to a mental health professional immediately.**")
    elif safety_level == "concern":
        st.warning("⚠️ **Moderate Concern**")
        st.info(response)
        st.info("💡 It may be helpful to talk to a trusted person or professional.")
    else:
        st.success("💬 Normal response")
        st.write(response)


def render_metric_card(label: str, value: str, delta: Optional[str] = None):
    """
    Render a metric card.
    
    Args:
        label: Metric label
        value: Metric value
        delta: Optional delta value
    """
    if delta:
        st.metric(label=label, value=value, delta=delta)
    else:
        st.metric(label=label, value=value)