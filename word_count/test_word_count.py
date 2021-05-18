import unittest
import word_count

class TestCase(unittest.TestCase):

    def test_word_count_1(self):
        self.assertEqual(word_count.word_count("Hello World, in-class activity 4"), 5)

    def test_word_count_2(self):
        self.assertEqual(word_count.word_count("Hello ? World"), 3)

    def test_word_count_3(self):
        self.assertEqual(word_count.word_count(" "), 1)
        
    def test_word_count_4(self):
        self.assertEqual(word_count.word_count(""), 0)
if __name__ == "__main__":
    unittest.main()