import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("J'ai de fortes opinions sur cet ensemble de classes IBM"),
             "I have strong opinions on this set of IBM classes")

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("I have strong opinions on this set of IBM classes"),
            "J'ai de fortes opinions sur cet ensemble de classes IBM")

unittest.main()
