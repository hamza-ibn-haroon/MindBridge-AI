import re
from typing import List


class PreprocessingEngine:

    def normalize(self, text: str) -> str:
        if not text:
            return ""

        text = text.lower().strip()

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text)

        # Keep letters, numbers, apostrophes and spaces
        text = re.sub(r"[^\w\s']", " ", text)

        text = re.sub(r"\s+", " ", text).strip()

        return text

    def tokenize(self, text: str) -> List[str]:
        normalized = self.normalize(text)

        if not normalized:
            return []

        return normalized.split()

    def preprocess(self, text: str) -> dict:
        normalized = self.normalize(text)
        tokens = self.tokenize(normalized)

        return {
            "original": text,
            "normalized": normalized,
            "tokens": tokens,
        }


preprocessor = PreprocessingEngine()