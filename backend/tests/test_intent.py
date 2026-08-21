"""Tests for intent detection."""

import unittest
from backend.services.preprocessing import preprocess_text
from backend.services.intent import get_intent_engine


class TestIntentDetection(unittest.TestCase):
    """Test intent detection functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.intent_engine = get_intent_engine()
    
    def test_greeting(self):
        """Test greeting detection."""
        processed = preprocess_text("Hello there!")
        result = self.intent_engine.detect_intent(processed)
        self.assertEqual(result["intent"], "greeting")
        self.assertGreater(result["confidence"], 0.5)
    
    def test_stress(self):
        """Test stress detection."""
        processed = preprocess_text("I'm really stressed out")
        result = self.intent_engine.detect_intent(processed)
        self.assertEqual(result["intent"], "stress")
        self.assertGreater(result["confidence"], 0.5)
    
    def test_academic_stress(self):
        """Test academic stress detection."""
        processed = preprocess_text("I'm stressed about my exams")
        result = self.intent_engine.detect_intent(processed)
        self.assertIn(result["intent"], ["academic_stress", "exam_stress"])
        self.assertGreater(result["confidence"], 0.5)
    
    def test_anxiety(self):
        """Test anxiety detection."""
        processed = preprocess_text("I feel anxious all the time")
        result = self.intent_engine.detect_intent(processed)
        self.assertEqual(result["intent"], "anxiety")
        self.assertGreater(result["confidence"], 0.5)
    
    def test_loneliness(self):
        """Test loneliness detection."""
        processed = preprocess_text("I feel so lonely")
        result = self.intent_engine.detect_intent(processed)
        self.assertEqual(result["intent"], "loneliness")
        self.assertGreater(result["confidence"], 0.5)
    
    def test_negation(self):
        """Test negation handling."""
        processed = preprocess_text("I am not stressed")
        result = self.intent_engine.detect_intent(processed)
        self.assertNotEqual(result["intent"], "stress")
        self.assertLess(result["confidence"], 0.3)
    
    def test_unknown_intent(self):
        """Test unknown intent detection."""
        processed = preprocess_text("The weather is nice today")
        result = self.intent_engine.detect_intent(processed)
        self.assertEqual(result["intent"], "unknown")
        self.assertLess(result["confidence"], 0.3)


if __name__ == "__main__":
    unittest.main()