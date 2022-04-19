import unittest
from jumble_solver import word_jumble_algorithm

class SimpleTest(unittest.TestCase):
    def test_word_jumble_algorithm(self):
        word: str = 'the'
        wordFile: str = 'corncob_lowercase.txt'
        resultList: list = word_jumble_algorithm(wordFile, word)
        testList: list = ('eh', 'the', 'he')

        # Sort alphabetically before comparing lists
        resultList = sorted(resultList)
        testList = sorted(testList)
        self.assertEqual(resultList, testList)

if __name__ == '__main__':
    unittest.main()