import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(None, None)
        self.assertEqual('Hello', 'Bonjour')
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(None, None)
        self.assertEqual('Bonjour', 'Hello')

unittest.main()