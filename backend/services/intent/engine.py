from .keywords import INTENT_KEYWORDS
from .phrases import INTENT_PHRASES
from .priorities import INTENT_PRIORITY


class IntentEngine:

    def __init__(self):
        self.keywords = INTENT_KEYWORDS
        self.phrases = INTENT_PHRASES
        self.priorities = INTENT_PRIORITY

    def _keyword_score(self, text: str, intent: str):
        score = 0
        matches = []

        for keyword, weight in self.keywords.get(intent, {}).items():

            if " " in keyword:
                if keyword in text:
                    score += weight
                    matches.append(keyword)
            else:
                words = text.split()

                if keyword in words:
                    score += weight
                    matches.append(keyword)

        return score, matches

    def _phrase_score(self, text: str, intent: str):
        score = 0
        matches = []

        for phrase in self.phrases.get(intent, []):

            if phrase.lower() in text:
                score += 4
                matches.append(phrase)

        return score, matches

    def _is_negated(self, text: str, keyword: str) -> bool:

        words = text.split()

        if keyword not in words:
            return False

        index = words.index(keyword)

        start = max(0, index - 3)

        previous_words = words[start:index]

        negations = {
            "not",
            "never",
            "no",
            "don't",
            "dont",
            "doesn't",
            "doesnt",
            "isn't",
            "isnt",
            "wasn't",
            "wasnt",
            "can't",
            "cant",
        }

        return any(word in negations for word in previous_words)

    def detect(self, text: str) -> dict:

        text = text.lower().strip()

        results = []

        for intent in self.keywords.keys():

            keyword_score, keyword_matches = self._keyword_score(
                text,
                intent,
            )

            phrase_score, phrase_matches = self._phrase_score(
                text,
                intent,
            )

            total_score = keyword_score + phrase_score

            if total_score > 0:

                results.append(
                    {
                        "intent": intent,
                        "score": total_score,
                        "priority": self.priorities.get(
                            intent,
                            0,
                        ),
                        "matched_keywords": keyword_matches,
                        "matched_phrases": phrase_matches,
                    }
                )

        if not results:
            return {
                "intent": "unknown",
                "confidence": 0.0,
                "matched_keywords": [],
                "matched_phrases": [],
                "competitors": [],
                "score_breakdown": {},
            }

        # Sort primarily by score, then priority
        results.sort(
            key=lambda item: (
                item["score"],
                item["priority"],
            ),
            reverse=True,
        )

        winner = results[0]

        # Basic confidence calculation
        confidence = min(
            0.99,
            0.50 + (winner["score"] / 20),
        )

        competitors = [
            {
                "intent": item["intent"],
                "score": item["score"],
            }
            for item in results[1:4]
        ]

        return {
            "intent": winner["intent"],
            "confidence": round(confidence, 2),
            "matched_keywords": winner["matched_keywords"],
            "matched_phrases": winner["matched_phrases"],
            "competitors": competitors,
            "score_breakdown": {
                item["intent"]: item["score"]
                for item in results
            },
        }


intent_engine = IntentEngine()