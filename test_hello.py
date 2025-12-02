"""
Unit tests for hello.py
"""
import unittest
from hello import greet

class TestHello(unittest.TestCase):
    """Test cases for the greet function"""
    
    def test_greet_default(self):
        """Test greeting with default name"""
        self.assertEqual(greet(), "Hello, World!")
    
    def test_greet_custom_name(self):
        """Test greeting with custom name"""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
    
    def test_greet_empty_string(self):
        """Test greeting with empty string"""
        self.assertEqual(greet(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()
