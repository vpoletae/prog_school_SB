import unittest
from Balanced_BST_2 import *

class Test_Balanced_BST(unittest.TestCase):

    def test_empty_array(self):
        array = []
        bst = BalancedBST()
        bst.GenerateTree(array)
        self.assertEqual(bst.Root, None)

    def test_unit_array(self):
        array = [1]
        bst = BalancedBST()
        bst.GenerateTree(array)
        self.assertEqual(bst.Root.NodeKey, 1)
        self.assertEqual(bst.Root.Parent, None)
        self.assertEqual(bst.Root.LeftChild, None)
        self.assertEqual(bst.Root.RightChild, None)
        self.assertEqual(bst.Root.Level, 1)

    def test_double_array(self):
        array = [1, 2]
        bst = BalancedBST()
        bst.GenerateTree(array)
        self.assertEqual(bst.Root.NodeKey, 1)
        self.assertEqual(bst.Root.Parent, None)
        self.assertEqual(bst.Root.LeftChild, None)
        self.assertEqual(bst.Root.Level, 1)
        self.assertEqual(bst.Root.RightChild.Parent.NodeKey, 1)
        self.assertEqual(bst.Root.RightChild.NodeKey, 2)
        self.assertEqual(bst.Root.RightChild.LeftChild, None)
        self.assertEqual(bst.Root.RightChild.RightChild, None)
        self.assertEqual(bst.Root.RightChild.Level, 2)

    def test_triple_array(self):
        array = [3, 1, 2]
        bst = BalancedBST()
        bst.GenerateTree(array)
        self.assertEqual(bst.Root.NodeKey, 2)
        self.assertEqual(bst.Root.Parent, None)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 1)
        self.assertEqual(bst.Root.RightChild.NodeKey, 3)
        self.assertEqual(bst.Root.Level, 1)
        self.assertEqual(bst.Root.RightChild.Parent.NodeKey, 2)
        self.assertEqual(bst.Root.LeftChild.Parent.NodeKey, 2)
        self.assertEqual(bst.Root.RightChild.LeftChild, None)
        self.assertEqual(bst.Root.RightChild.RightChild, None)
        self.assertEqual(bst.Root.LeftChild.LeftChild, None)
        self.assertEqual(bst.Root.LeftChild.RightChild, None)
        self.assertEqual(bst.Root.RightChild.Level, 2)
        self.assertEqual(bst.Root.LeftChild.Level, 2)

    def test_7_array(self):
        array = [3,2,1,4,5,6,7]
        bst = BalancedBST()
        bst.GenerateTree(array)
        self.assertEqual(bst.Root.NodeKey, 4)
        self.assertEqual(bst.Root.Parent, None)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 2)
        self.assertEqual(bst.Root.RightChild.NodeKey, 6)
        self.assertEqual(bst.Root.Level, 1)
        self.assertEqual(bst.Root.RightChild.Parent.NodeKey, 4)
        self.assertEqual(bst.Root.LeftChild.Parent.NodeKey, 4)
        self.assertEqual(bst.Root.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.RightChild.RightChild.NodeKey, 7)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(bst.Root.LeftChild.LeftChild.Parent.NodeKey, 2)
        self.assertEqual(bst.Root.RightChild.Level, 2)
        self.assertEqual(bst.Root.LeftChild.Level, 2)
        self.assertEqual(bst.Root.RightChild.RightChild.Level, 3)
        self.assertEqual(bst.Root.RightChild.LeftChild.Level, 3)
        self.assertEqual(bst.Root.LeftChild.RightChild.Level, 3)
        self.assertEqual(bst.Root.LeftChild.LeftChild.Level, 3)
        self.assertEqual(bst.IsBalanced(), True)

    def test_balanced(self):
        array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        bst = BalancedBST()
        bst.GenerateTree(array)
        self.assertEqual(bst.IsBalanced(), True)

    def test_disbalanced(self):
        array = [1,2,3,4,5,6,7,8]
        bst = BalancedBST()
        bst.GenerateTree(array)
        node_9 = BSTNode(9, bst.Root.RightChild.RightChild.RightChild)
        node_9.Level = 5
        bst.Root.RightChild.RightChild.RightChild.RightChild = node_9
        print(bst.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(bst.IsBalanced(), False)

if __name__ == '__main__':
    unittest.main()
