"""
Tests for english_to_french and french_to_english
"""
import unittest
from machinetranslation import translator

class TestEnglishToFrench(unittest.TestCase):
    """
    Tests for english_to_french
    """
    def test_1(self):
        """
        Test cases for null and valid value
        """
        self.assertEqual(None, None)
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    """
    Tests for french_to_english
    """
    def test_1(self):
        """
        Test cases for null and valid value
        """
        self.assertEqual(None, None)
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

unittest.main()
