import unittest
from BinaryTree import BSTNode, BSTFind, BST

class Test_BinaryTree(unittest.TestCase):

    def test_find_node(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        add_2 = (2, 2)
        add_3 = (3, 3)
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        self.assertEqual(binary_tree.FindNodeByKey(1).Node.NodeKey, 1)
        self.assertEqual(binary_tree.FindNodeByKey(1).Node.RightChild.NodeKey, 2)
        self.assertEqual(binary_tree.FindNodeByKey(1).Node.LeftChild, None)
        self.assertEqual(binary_tree.Root.NodeKey, 1)
        self.assertEqual(binary_tree.FindNodeByKey(2).Node.NodeKey, 2)
        self.assertEqual(binary_tree.FindNodeByKey(2).Node.RightChild.NodeKey, 3)
        self.assertEqual(binary_tree.FindNodeByKey(3).Node.NodeKey, 3)
        add_4 = (100, 100)
        add_5 = (50, 50)
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        binary_tree.AddKeyValue(add_5[0], add_5[1])
        self.assertEqual(binary_tree.FindNodeByKey(3).Node.RightChild.NodeKey, 100)
        self.assertEqual(binary_tree.FindNodeByKey(100).Node.LeftChild.NodeKey, 50)
        add_6 = (100, 100)
        binary_tree.AddKeyValue(add_6[0], add_6[1])
        self.assertEqual(binary_tree.FindNodeByKey(50).Node.RightChild, None)

    def test_find_root_max(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        root = binary_tree.FindNodeByKey(1).Node
        self.assertEqual(binary_tree.FinMinMax(FromNode=root, FindMax=True).NodeKey, 4)

    def test_find_root_min(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        root = binary_tree.FindNodeByKey(1).Node
        self.assertEqual(binary_tree.FinMinMax(FromNode=root, FindMax=False).NodeKey, 1)

    def test_find_tree_max(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        subTree = binary_tree.FindNodeByKey(3).Node
        self.assertEqual(binary_tree.FinMinMax(FromNode=subTree, FindMax=True).NodeKey, 4)

    def test_find_tree_min(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        subTree = binary_tree.FindNodeByKey(3).Node
        self.assertEqual(binary_tree.FinMinMax(FromNode=subTree, FindMax=False).NodeKey, 2)

    def test_delete_leaf(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        binary_tree.DeleteNodeByKey(4)
        root = binary_tree.FindNodeByKey(1).Node
        self.assertEqual(binary_tree.FinMinMax(FromNode=root, FindMax=True).NodeKey, 3)
        self.assertEqual(binary_tree.FindNodeByKey(3).Node.RightChild, None)
        self.assertEqual(binary_tree.FindNodeByKey(3).Node.LeftChild.NodeKey, 2)

    def test_delete_node(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        binary_tree.DeleteNodeByKey(3)
        root = binary_tree.FindNodeByKey(1).Node
        self.assertEqual(binary_tree.FinMinMax(FromNode=root, FindMax=True).NodeKey, 4)
        self.assertEqual(binary_tree.FindNodeByKey(1).Node.RightChild.NodeKey, 4)
        self.assertEqual(binary_tree.FindNodeByKey(4).Node.LeftChild.NodeKey, 2)
        self.assertEqual(binary_tree.FindNodeByKey(4).Node.RightChild, None)
        add_5 = (1.5, 1.5)
        binary_tree.AddKeyValue(add_5[0], add_5[1])
        binary_tree.DeleteNodeByKey(4)
        self.assertEqual(binary_tree.FinMinMax(FromNode=root, FindMax=True).NodeKey, 2)
        self.assertEqual(binary_tree.FindNodeByKey(1).Node.RightChild.NodeKey, 2)
        self.assertEqual(binary_tree.FindNodeByKey(2).Node.LeftChild.NodeKey, 1.5)
        self.assertEqual(binary_tree.FindNodeByKey(2).Node.RightChild, None)

    def test_delete_root(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        binary_tree.DeleteNodeByKey(1)
        self.assertEqual(binary_tree.Root.NodeKey, 3)

    def test_count(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        add_2 = (3, 3)
        add_3 = (2, 2)
        add_4 = (4, 4)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        binary_tree.AddKeyValue(add_3[0], add_3[1])
        binary_tree.AddKeyValue(add_4[0], add_4[1])
        self.assertEqual(binary_tree.Count(), 4)
        # self.assertEqual(binary_tree.Count(), 4)
        binary_tree.DeleteNodeByKey(1)
        self.assertEqual(binary_tree.Root.NodeKey, 3)
        self.assertEqual(binary_tree.Count(), 3)

    def test_count_zero(self):
        binary_tree = BST(None)
        self.assertEqual(binary_tree.Count(), 0)
        add_1 = (1, 1)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        self.assertEqual(binary_tree.Count(), 1)
        add_2 = (3, 3)
        binary_tree.AddKeyValue(add_2[0], add_2[1])
        self.assertEqual(binary_tree.Count(), 2)
        binary_tree.DeleteNodeByKey(3)
        self.assertEqual(binary_tree.Count(), 1)
        binary_tree.DeleteNodeByKey(1)
        self.assertEqual(binary_tree.Count(), 0)

    def test_count_one(self):
        binary_tree = BST(None)
        add_1 = (1, 1)
        binary_tree.AddKeyValue(add_1[0], add_1[1])
        self.assertEqual(binary_tree.Count(), 1)

if __name__ == '__main__':
    unittest.main()
