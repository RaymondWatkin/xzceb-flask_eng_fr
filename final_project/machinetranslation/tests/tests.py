import unittest
from translator import english_to_french, french_to_english

class TranslationTestsEnglish2French(unittest.TestCase):
    def Test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TranslationTestsFrench2English(unittest.TestCase):
    def Test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')


unittest.main()