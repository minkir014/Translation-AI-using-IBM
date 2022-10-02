"""
This is for unit test of the Module translation
"""

import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    This class tests the English to French Translation
    """

    def test(self):
        """
        This Function holds the tests for English to French Translation
        """

        self.assertEqual(english_to_french("Hello"), "Bonjour",
                         "Failed to translate 'Hello'")
        self.assertNotEqual(english_to_french("Hey, how are you?"),
                            "Salut, Comment tu es?", "Punctuation Problem")
        self.assertEqual(english_to_french("How are you?"),
                         "Comment es-tu?", "Failed to translate 'How are you?'")


class TestFrenchToEnglish(unittest.TestCase):
    """
    This class tests the French to English Translation
    """

    def test(self):
        """
        This Function holds the tests for the French to English Translations
        """

        self.assertEqual(french_to_english("Bonjour"), "Hello",
                         "Failed to translate 'Bonjour'")
        self.assertNotEqual(french_to_english("Salut, comment tu es?"),
                            "Hello, How are you?", "Puncuation Error")
        self.assertEqual(french_to_english("Comment es-tu?"), "How are you?",
                         "Failed to translate 'Comment es-tu?'")


unittest.main()
