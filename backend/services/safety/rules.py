HIGH_RISK_PATTERNS = [
    "hurt myself",
    "harm myself",
    "kill myself",
    "end my life",
    "want to die",
    "suicide",
    "suicidal",
    "self harm",
    "self-harm",
]


CONCERN_PATTERNS = [
    "can't cope",
    "cannot cope",
    "feel hopeless",
    "completely hopeless",
    "feel worthless",
    "nothing matters",
    "i give up",
]


SAFETY_RESPONSES = {
    "high_risk": (
        "I'm really sorry you're going through something this intense. "
        "Your safety matters, and this is a situation where support from "
        "a trusted person or qualified professional is important. "
        "If you may be in immediate danger, please contact your local "
        "emergency service or go to the nearest emergency department."
    ),

    "concern": (
        "It sounds like things may be feeling especially difficult right now. "
        "You don't have to handle everything alone. Consider reaching out to "
        "someone you trust and taking things one small step at a time."
    ),
}