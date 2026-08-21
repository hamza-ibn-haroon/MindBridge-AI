"""Tests for safety detection."""

import unittest
from backend.services.preprocessing import preprocess_text
from backend.services.safety import get_safety_engine
from backend.shared.constants import SAFETY_NORMAL, SAFETY_CONCERN, SAFETY_HIGH_RISK


class TestSafetyEngine(unittest.TestCase):
    """Test safety detection functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.safety_engine = get_safety_engine()
    
    def test_normal_safety(self):
        """Test normal safety level."""
        processed = preprocess_text("I'm feeling okay today")
        result = self.safety_engine.analyze(processed)
        self.assertEqual(result["level"], SAFETY_NORMAL)
        self.assertFalse(result["is_high_risk"])
        self.assertFalse(result["is_concern"])
    
    def test_concern_safety(self):
        """Test concern safety level."""
        processed = preprocess_text("I'm feeling overwhelmed and can't cope")
        result = self.safety_engine.analyze(processed)
        self.assertEqual(result["level"], SAFETY_CONCERN)
        self.assertTrue(result["is_concern"])
    
    def test_high_risk_safety(self):
        """Test high-risk safety level."""
        processed = preprocess_text("I want to kill myself")
        result = self.safety_engine.analyze(processed)
        self.assertEqual(result["level"], SAFETY_HIGH_RISK)
        self.assertTrue(result["is_high_risk"])
    
    def test_high_risk_pattern_matching(self):
        """Test high-risk pattern matching."""
        processed = preprocess_text("I've been thinking about suicide")
        result = self.safety_engine.analyze(processed)
        self.assertEqual(result["level"], SAFETY_HIGH_RISK)
        self.assertGreater(len(result["detected_patterns"]), 0)


if __name__ == "__main__":
    unittest.main()