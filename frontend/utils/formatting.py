"""
Formatting utilities for displaying data in the UI.
"""

from typing import Dict, Any, List, Optional


def format_intent_name(intent: Optional[str]) -> str:
    """
    Format an intent key into a human-readable display name.
    
    Args:
        intent: The intent key (e.g., "academic_stress")
        
    Returns:
        Formatted display name (e.g., "Academic Stress")
    """
    if not intent:
        return "Unknown"
    
    # Define friendly names for common intents
    intent_names = {
        "academic_stress": "Academic Stress",
        "anxiety": "Anxiety",
        "depression": "Depression",
        "loneliness": "Loneliness",
        "motivation": "Motivation",
        "stress": "Stress",
        "burnout": "Burnout",
        "work_stress": "Work Stress",
        "relationship": "Relationship Issues",
        "sleep": "Sleep Issues",
        "general": "General Support"
    }
    
    if intent in intent_names:
        return intent_names[intent]
    
    # Fallback: convert snake_case to Title Case
    return intent.replace("_", " ").title()


def format_confidence(confidence: Optional[float]) -> str:
    """
    Format confidence score as a percentage.
    
    Args:
        confidence: Confidence score (0-1)
        
    Returns:
        Formatted percentage string
    """
    if confidence is None:
        return "N/A"
    
    try:
        percentage = confidence * 100
        return f"{percentage:.0f}%"
    except (TypeError, ValueError):
        return "N/A"


def format_safety_label(safety_level: Optional[str]) -> str:
    """
    Format safety level with appropriate emoji and styling.
    
    Args:
        safety_level: "normal", "concern", or "high_risk"
        
    Returns:
        Tuple of (label, emoji) if returning tuple
        Formatted string if returning string
    """
    if not safety_level:
        return "Unknown"
    
    labels = {
        "normal": ("Normal", "🟢"),
        "concern": ("Moderate Concern", "🟡"),
        "high_risk": ("High Risk", "🔴")
    }
    
    if safety_level in labels:
        return f"{labels[safety_level][1]} {labels[safety_level][0]}"
    
    return f"Unknown ({safety_level})"


def format_score(score: Optional[float], label: Optional[str] = None) -> str:
    """
    Format a score as a percentage.
    
    Args:
        score: Score value (0-1 or 0-100)
        label: Optional label to prepend
        
    Returns:
        Formatted score string
    """
    if score is None:
        return "N/A"
    
    try:
        # If score is between 0 and 1, treat as percentage
        if 0 <= score <= 1:
            percentage = score * 100
        else:
            percentage = score
        
        formatted = f"{percentage:.0f}%"
        if label:
            return f"{label}: {formatted}"
        return formatted
    except (TypeError, ValueError):
        return "N/A"


def format_entities(entities: Optional[Dict[str, Any]]) -> str:
    """
    Format entity dictionary into a readable string.
    
    Args:
        entities: Entity dictionary from the API
        
    Returns:
        Formatted entity string
    """
    if not entities:
        return "No entities detected"
    
    formatted = []
    for key, value in entities.items():
        if isinstance(value, list):
            value_str = ", ".join(str(v) for v in value)
        else:
            value_str = str(value)
        
        # Make key human-readable
        key_readable = key.replace("_", " ").title()
        formatted.append(f"{key_readable}: {value_str}")
    
    return " | ".join(formatted)


def get_confidence_color(confidence: Optional[float]) -> str:
    """
    Get a color based on confidence level.
    
    Args:
        confidence: Confidence score (0-1)
        
    Returns:
        CSS color string
    """
    if confidence is None:
        return "gray"
    
    try:
        if confidence >= 0.8:
            return "green"
        elif confidence >= 0.5:
            return "orange"
        else:
            return "red"
    except (TypeError, ValueError):
        return "gray"


def get_safety_color(safety_level: Optional[str]) -> str:
    """
    Get a color based on safety level.
    
    Args:
        safety_level: "normal", "concern", or "high_risk"
        
    Returns:
        CSS color string
    """
    if not safety_level:
        return "gray"
    
    colors = {
        "normal": "green",
        "concern": "orange",
        "high_risk": "red"
    }
    
    return colors.get(safety_level, "gray")


def truncate_text(text: str, max_length: int = 200) -> str:
    """
    Truncate text to a maximum length with ellipsis.
    
    Args:
        text: The text to truncate
        max_length: Maximum length before truncation
        
    Returns:
        Truncated text
    """
    if not text:
        return ""
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length] + "..."