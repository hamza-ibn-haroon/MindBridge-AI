from collections import defaultdict


class SessionMemory:

    def __init__(self, max_messages: int = 10):

        self.max_messages = max_messages

        self.sessions = defaultdict(
            lambda: {
                "messages": [],
                "last_intent": None,
                "last_entities": {},
                "last_safety_level": "normal",
            }
        )

    def get(self, session_id: str) -> dict:

        return self.sessions[session_id]

    def add_message(
        self,
        session_id: str,
        role: str,
        content: str,
    ):

        session = self.sessions[session_id]

        session["messages"].append(
            {
                "role": role,
                "content": content,
            }
        )

        session["messages"] = session["messages"][
            -self.max_messages:
        ]

    def update_analysis(
        self,
        session_id: str,
        intent: str,
        entities: dict,
        safety_level: str,
    ):

        session = self.sessions[session_id]

        session["last_intent"] = intent
        session["last_entities"] = entities
        session["last_safety_level"] = safety_level

    def clear(self, session_id: str):

        if session_id in self.sessions:
            del self.sessions[session_id]


session_memory = SessionMemory()