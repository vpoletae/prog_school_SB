import unittest
from BinarySearch import aBST

class Test_BinaryTree(unittest.TestCase):

    def test_add_search(self):
        binary_tree = aBST(6)
        self.assertEqual(len(binary_tree.Tree), 7)
        self.assertEqual(binary_tree.AddKey(11), 0)
        self.assertEqual(binary_tree.FindKeyIndex(11), 0)
        self.assertEqual(binary_tree.FindKeyIndex(6), -1)
        self.assertEqual(binary_tree.AddKey(6), 1)
        self.assertEqual(binary_tree.FindKeyIndex(13), -2)
        self.assertEqual(binary_tree.AddKey(13), 2)
        self.assertEqual(binary_tree.FindKeyIndex(4), -3)
        self.assertEqual(binary_tree.AddKey(4), 3)
        self.assertEqual(binary_tree.FindKeyIndex(7), -4)
        self.assertEqual(binary_tree.AddKey(7), 4)
        self.assertEqual(binary_tree.FindKeyIndex(12), -5)
        self.assertEqual(binary_tree.AddKey(12), 5)
        self.assertEqual(binary_tree.FindKeyIndex(14), -6)
        self.assertEqual(binary_tree.AddKey(14), 6)
        self.assertEqual(binary_tree.FindKeyIndex(15), None)
        self.assertEqual(binary_tree.AddKey(15), -1)

if __name__ == '__main__':
    unittest.main()
