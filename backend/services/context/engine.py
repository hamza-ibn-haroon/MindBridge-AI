from .memory import session_memory


class ContextEngine:

    def get_context(self, session_id: str) -> dict:

        return session_memory.get(session_id)

    def add_user_message(
        self,
        session_id: str,
        message: str,
    ):

        session_memory.add_message(
            session_id,
            "user",
            message,
        )

    def add_assistant_message(
        self,
        session_id: str,
        message: str,
    ):

        session_memory.add_message(
            session_id,
            "assistant",
            message,
        )

    def update(
        self,
        session_id: str,
        intent: str,
        entities: dict,
        safety_level: str,
    ):

        session_memory.update_analysis(
            session_id,
            intent,
            entities,
            safety_level,
        )


context_engine = ContextEngine()