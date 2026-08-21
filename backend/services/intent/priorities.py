"""Priority definitions for MindBridge intent resolution."""

from typing import Dict


# Higher number = higher priority.
# Specific and safety-related intents should win over
# broader/general intents when multiple matches are detected.

INTENT_PRIORITY: Dict[str, int] = {

    # =========================================================
    # HIGH-RISK / SAFETY
    # =========================================================

    "help_request": 100,


    # =========================================================
    # SPECIFIC STRESS TYPES
    # =========================================================

    "exam_stress": 90,
    "academic_stress": 85,
    "work_stress": 85,
    "career_stress": 85,
    "relationship_stress": 85,


    # =========================================================
    # EMOTIONAL STATES
    # =========================================================

    "burnout": 80,
    "anxiety": 80,
    "anger": 80,


    # =========================================================
    # GENERAL STATES
    # =========================================================

    "stress": 70,
    "sadness": 70,
    "loneliness": 70,
    "low_motivation": 70,
    "sleep_problem": 70,


    # =========================================================
    # COPING / SUPPORT
    # =========================================================

    "coping_request": 75,
    "general_support": 65,


    # =========================================================
    # BASIC CONVERSATION
    # =========================================================

    "greeting": 50,
    "goodbye": 50,
    "gratitude": 50,


    # =========================================================
    # FALLBACK
    # =========================================================

    "unknown": 10,
}


def get_priority(intent: str) -> int:
    """
    Return the priority of an intent.

    Unknown intents receive priority 10.
    """

    return INTENT_PRIORITY.get(intent, 10)


def get_priorities() -> Dict[str, int]:
    """
    Return the complete intent-priority mapping.
    """

    return INTENT_PRIORITY