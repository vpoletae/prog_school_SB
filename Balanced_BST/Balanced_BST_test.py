import unittest
from Balanced_BST import *

class Test_Balanced_BST(unittest.TestCase):

    # def test_empty_array(self):
    #     array = []
    #     self.assertEqual(GenerateBBSTArray(array), [])

    # def test_unit_array(self):
    #     array = [1]
    #     self.assertEqual(GenerateBBSTArray(array), [1])

    # def test_triple_array(self):
    #     array = [3,2,1]
    #     self.assertEqual(GenerateBBSTArray(array), [2,1,3])

    # def test_7_array(self):
    #     array = [3,2,1,4,5,6,7]
    #     self.assertEqual(GenerateBBSTArray(array), [4,2,6,1,3,5,7])

    def test_15_array(self):
        array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(GenerateBBSTArray(array), [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15])

if __name__ == '__main__':
    unittest.main()
