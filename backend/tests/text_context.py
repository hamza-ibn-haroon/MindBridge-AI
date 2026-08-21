"""Tests for context management."""

import unittest
from backend.services.context import get_context_engine


class TestContextEngine(unittest.TestCase):
    """Test context management functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.context_engine = get_context_engine()
    
    def test_create_session(self):
        """Test session creation."""
        session_id = self.context_engine.get_or_create_session(None)
        self.assertIsNotNone(session_id)
        self.assertIsInstance(session_id, str)
    
    def test_reuse_session(self):
        """Test session reuse."""
        session_id = self.context_engine.get_or_create_session(None)
        same_session = self.context_engine.get_or_create_session(session_id)
        self.assertEqual(session_id, same_session)
    
    def test_update_context(self):
        """Test context update."""
        session_id = self.context_engine.get_or_create_session(None)
        result = self.context_engine.update_context(
            session_id, 
            "Test message", 
            "test_intent", 
            {"test": "entity"}
        )
        self.assertTrue(result)
    
    def test_get_context(self):
        """Test context retrieval."""
        session_id = self.context_engine.get_or_create_session(None)
        self.context_engine.update_context(
            session_id, 
            "Test message", 
            "test_intent", 
            {"test": "entity"}
        )
        context = self.context_engine.get_context(session_id)
        self.assertIsNotNone(context)
        self.assertTrue(context.get("has_history", False))


if __name__ == "__main__":
    unittest.main()