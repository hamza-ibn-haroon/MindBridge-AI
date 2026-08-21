"""Tests for entity extraction."""

import unittest
from backend.services.preprocessing import preprocess_text
from backend.services.entity import get_entity_engine


class TestEntityEngine(unittest.TestCase):
    """Test entity extraction functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.entity_engine = get_entity_engine()
    
    def test_academic_entity(self):
        """Test academic entity extraction."""
        processed = preprocess_text("I have exams next week")
        result = self.entity_engine.extract_entities(processed)
        self.assertIn("academic", result["categories"])
        self.assertTrue(result["has_entities"])
    
    def test_work_entity(self):
        """Test work entity extraction."""
        processed = preprocess_text("My work deadlines are piling up")
        result = self.entity_engine.extract_entities(processed)
        self.assertIn("work", result["categories"])
        self.assertTrue(result["has_entities"])
    
    def test_sleep_entity(self):
        """Test sleep entity extraction."""
        processed = preprocess_text("I can't sleep at night")
        result = self.entity_engine.extract_entities(processed)
        self.assertIn("sleep", result["categories"])
        self.assertTrue(result["has_entities"])
    
    def test_multiple_entities(self):
        """Test multiple entity extraction."""
        processed = preprocess_text("I'm stressed about work and exams")
        result = self.entity_engine.extract_entities(processed)
        self.assertGreater(len(result["categories"]), 0)
        self.assertTrue(result["has_entities"])


if __name__ == "__main__":
    unittest.main()