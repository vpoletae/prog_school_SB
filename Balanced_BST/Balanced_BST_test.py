import unittest
from Balanced_BST import *

class Test_Balanced_BST(unittest.TestCase):

    def test_empty_array(self):
        array = []
        self.assertEqual(GenerateBBSTArray(array), [])

    def test_unit_array(self):
        array = [1]
        self.assertEqual(GenerateBBSTArray(array), [1])

    def test_double_array(self):
        array = [2,1]
        self.assertEqual(GenerateBBSTArray(array), [1,2])

    def test_triple_array(self):
        array = [3,2,1]
        self.assertEqual(GenerateBBSTArray(array), [2,1,3])

    def test_7_array(self):
        array = [3,2,1,4,5,6,7]
        self.assertEqual(GenerateBBSTArray(array), [4,2,1,3,6,5,7])

if __name__ == '__main__':
    unittest.main()
