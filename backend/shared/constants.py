"""Shared constants for MindBridge."""

MAX_MESSAGE_LENGTH = 2000
DEFAULT_SESSION_EXPIRY = 3600  # 1 hour
MAX_SESSION_HISTORY = 10

# Safety levels
SAFETY_NORMAL = "normal"
SAFETY_CONCERN = "concern"
SAFETY_HIGH_RISK = "high_risk"

# Intent categories
INTENT_GREETING = "greeting"
INTENT_GOODBYE = "goodbye"
INTENT_GENERAL_SUPPORT = "general_support"
INTENT_STRESS = "stress"
INTENT_ACADEMIC_STRESS = "academic_stress"
INTENT_WORK_STRESS = "work_stress"
INTENT_EXAM_STRESS = "exam_stress"
INTENT_ANXIETY = "anxiety"
INTENT_LONELINESS = "loneliness"
INTENT_SADNESS = "sadness"
INTENT_LOW_MOTIVATION = "low_motivation"
INTENT_SLEEP_PROBLEM = "sleep_problem"
INTENT_RELATIONSHIP_STRESS = "relationship_stress"
INTENT_CAREER_STRESS = "career_stress"
INTENT_BURNOUT = "burnout"
INTENT_ANGER = "anger"
INTENT_GRATITUDE = "gratitude"
INTENT_HELP_REQUEST = "help_request"
INTENT_COPING_REQUEST = "coping_request"
INTENT_UNKNOWN = "unknown"