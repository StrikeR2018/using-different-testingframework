import unittest
import palindrome

class TestCase(unittest.TestCase):

    def test_palindrome_1(self):
        self.assertEqual(palindrome.checkUserInput("String"), False)
    
    def test_palindrome_2(self):
        self.assertEqual(palindrome.checkUserInput("StringgnirtS"), True)
    
    def test_palindrome_3(self):
        self.assertEqual(palindrome.checkUserInput("Stringgnirts"), True)

    def test_palindrome_3(self):
        self.assertEqual(palindrome.checkUserInput("String?gnirtS"), True)
if __name__ == "__main__":
    unittest.main()
