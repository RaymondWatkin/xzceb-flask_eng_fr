import unittest
from translator import english_to_french, french_to_english

class TranslationTestsEnglish2French(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('hello'), 'hello')

class TranslationTestsFrench2English(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

if __name__ == '__main__':
    unittest.main()