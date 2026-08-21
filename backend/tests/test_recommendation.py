"""Tests for recommendation generation."""

import unittest
from backend.services.recommendation import get_recommendation_engine
from backend.services.preprocessing import preprocess_text
from backend.services.intent import get_intent_engine
from backend.services.safety import get_safety_engine
from backend.services.entity import get_entity_engine
from backend.services.context import get_context_engine


class TestRecommendationEngine(unittest.TestCase):
    """Test recommendation generation functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.recommendation_engine = get_recommendation_engine()
        self.intent_engine = get_intent_engine()
        self.safety_engine = get_safety_engine()
        self.entity_engine = get_entity_engine()
        self.context_engine = get_context_engine()
    
    def test_stress_recommendations(self):
        """Test stress recommendations."""
        processed = preprocess_text("I'm stressed")
        intent = self.intent_engine.detect_intent(processed)
        safety = self.safety_engine.analyze(processed)
        entities = self.entity_engine.extract_entities(processed)
        context = {"has_history": False}
        
        recommendations = self.recommendation_engine.generate_recommendations(
            intent, safety, entities, context
        )
        self.assertGreater(len(recommendations), 0)
        self.assertIsInstance(recommendations, list)
    
    def test_academic_recommendations(self):
        """Test academic stress recommendations."""
        processed = preprocess_text("I have exams coming up")
        intent = self.intent_engine.detect_intent(processed)
        safety = self.safety_engine.analyze(processed)
        entities = self.entity_engine.extract_entities(processed)
        context = {"has_history": False}
        
        recommendations = self.recommendation_engine.generate_recommendations(
            intent, safety, entities, context
        )
        self.assertGreater(len(recommendations), 0)
    
    def test_anxiety_recommendations(self):
        """Test anxiety recommendations."""
        processed = preprocess_text("I feel anxious")
        intent = self.intent_engine.detect_intent(processed)
        safety = self.safety_engine.analyze(processed)
        entities = self.entity_engine.extract_entities(processed)
        context = {"has_history": False}
        
        recommendations = self.recommendation_engine.generate_recommendations(
            intent, safety, entities, context
        )
        self.assertGreater(len(recommendations), 0)


if __name__ == "__main__":
    unittest.main()