import unittest
from Black_tree import *

class Test_Black_tree(unittest.TestCase):

    def test_even_empty_tree(self):
        tree = SimpleTree(None)
        self.assertEqual(tree.EvenTrees(), [])

    def test_even_unit_tree(self):
        # add first to empty
        node1 = SimpleTreeNode('a', None)
        tree = SimpleTree(None)
        tree.AddChild(None, node1)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [])
        self.assertEqual(tree.EvenTrees(), [])

    def test_even_no_trees_line(self):
        # add second
        node1 = SimpleTreeNode('a', None)
        tree = SimpleTree(None)
        tree.AddChild(None, node1)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [])
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [node2])
        self.assertEqual(node2.Parent, node1)
        self.assertEqual(node2.Children, [])
        # add third to second
        node3 = SimpleTreeNode('c', node2)
        tree.AddChild(node2, node3)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.Children, [node2])
        self.assertEqual(node2.Children, [node3])
        self.assertEqual(node3.Parent, node2)
        self.assertEqual(node3.Children, [])
        self.assertEqual(tree.EvenTrees(), [])

    def test_even_no_trees_pyr(self):
        # add second
        node1 = SimpleTreeNode('a', None)
        tree = SimpleTree(None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        # add third to second
        node3 = SimpleTreeNode('c', node1)
        tree.AddChild(node1, node3)
        self.assertEqual(tree.EvenTrees(), [])

    def test_even_one_tree(self):
        node1 = SimpleTreeNode('a', None)
        tree = SimpleTree(None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode('c', node1)
        tree.AddChild(node1, node3)
        node4 = SimpleTreeNode('d', node2)
        tree.AddChild(node2, node4)
        # self.assertEqual(tree.EvenTrees(), [node1, node2])
        node5 = SimpleTreeNode('e', node2)
        tree.AddChild(node2, node5)
        # self.assertEqual(tree.EvenTrees(), [])
        node6 = SimpleTreeNode('f', node5)
        tree.AddChild(node5, node6)
        # self.assertEqual(tree.EvenTrees(), [node2, node5, node1, node2])
        node7 = SimpleTreeNode('g', node6)
        tree.AddChild(node6, node7)
        self.assertEqual(tree.EvenTrees(), [node5, node6])

    def test_base(self):
        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode(2, node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, node1)
        tree.AddChild(node1, node3)
        node4 = SimpleTreeNode(6, node1)
        tree.AddChild(node1, node4)
        node5 = SimpleTreeNode(5, node2)
        tree.AddChild(node2, node5)
        node6 = SimpleTreeNode(7, node2)
        tree.AddChild(node2, node6)
        node8 = SimpleTreeNode(4, node3)
        tree.AddChild(node3, node8)
        node9 = SimpleTreeNode(8, node4)
        tree.AddChild(node4, node9)
        node10 = SimpleTreeNode(9, node9)
        tree.AddChild(node9, node10)
        node11 = SimpleTreeNode(10, node9)
        tree.AddChild(node9, node11)
        self.assertEqual(tree.EvenTrees(), [node1, node4, node1, node3])


if __name__ == '__main__':
    unittest.main()
