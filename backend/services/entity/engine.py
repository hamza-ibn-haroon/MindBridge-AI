from .entities import ENTITY_GROUPS


class EntityEngine:

    def extract(self, text: str) -> dict:

        text = text.lower()

        detected = {}

        for category, keywords in ENTITY_GROUPS.items():

            matches = []

            for keyword in keywords:

                if keyword in text:
                    matches.append(keyword)

            if matches:
                detected[category] = list(set(matches))

        topic = None
        trigger = None

        if "academic" in detected:
            topic = "academic"

            academic_terms = detected["academic"]

            if "exam" in academic_terms or "exams" in academic_terms:
                trigger = "exam"

            elif "assignment" in academic_terms:
                trigger = "assignment"

        elif "work" in detected:
            topic = "work"

            work_terms = detected["work"]

            if "deadline" in work_terms or "deadlines" in work_terms:
                trigger = "deadline"

            elif "workload" in work_terms:
                trigger = "workload"

        elif "relationship" in detected:
            topic = "relationship"

        elif "career" in detected:
            topic = "career"

        elif "sleep" in detected:
            topic = "sleep"

        return {
            "topic": topic,
            "trigger": trigger,
            "entities": detected,
        }


entity_engine = EntityEngine()