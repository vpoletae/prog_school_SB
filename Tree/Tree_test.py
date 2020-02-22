import unittest
from Tree import SimpleTreeNode, SimpleTree

class Test_SimpleTree(unittest.TestCase):

    def test_add_child(self):
        # add first to empty
        node1 = SimpleTreeNode('a', None)
        tree = SimpleTree(None)
        tree.AddChild(None, node1)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [])
        # add second
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
        # add fourth to first
        node4 = SimpleTreeNode('d', node1)
        tree.AddChild(node1, node4)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.Children, [node2, node4])
        self.assertEqual(node4.Parent, node1)
        self.assertEqual(node4.Children, [])
        self.assertEqual(node3.Parent, node2)
        self.assertEqual(node3.Children, [])

    def test_get_all_nodes(self):
        # empty
        tree = SimpleTree(None)
        nodes = tree.GetAllNodes()
        self.assertEqual(nodes, [None])
        # full
        node1 = SimpleTreeNode('a', None)
        tree = SimpleTree(None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode('c', node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode('d', node1)
        tree.AddChild(node1, node4)
        nodes = tree.GetAllNodes()
        self.assertEqual(nodes, [node1, node2, node3, node4])

    def test_delete_node(self):
        # from empty
        tree = SimpleTree(None)
        node_to_del = SimpleTreeNode('a', None)
        tree.DeleteNode(node_to_del)
        self.assertEqual(tree.Root, None)
        # from unitary
        node1 = SimpleTreeNode('a', None)
        tree.AddChild(None, node1)
        tree.DeleteNode(node_to_del)
        self.assertEqual(tree.Root, None)
        # del non-existing
        node_to_del = SimpleTreeNode('1', None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode('c', node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode('d', node1)
        tree.AddChild(node1, node4)
        tree.DeleteNode(node_to_del)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [node2, node4])
        self.assertEqual(node2.Parent, node1)
        self.assertEqual(node2.Children, [node3])
        self.assertEqual(node3.Parent, node2)
        self.assertEqual(node3.Children, [])
        self.assertEqual(node4.Parent, node1)
        self.assertEqual(node4.Children, [])
        # del existing leaf
        leaf_to_del = SimpleTreeNode('c', None)
        tree.DeleteNode(leaf_to_del)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [node2, node4])
        self.assertEqual(node2.Parent, node1)
        self.assertEqual(node2.Children, [])
        self.assertEqual(node3.Parent, None)
        self.assertEqual(node3.Children, [])
        self.assertEqual(node4.Parent, node1)
        self.assertEqual(node4.Children, [])
        # del existing node
        tree.AddChild(node2, node3)
        node_to_del = SimpleTreeNode('b', None)
        tree.DeleteNode(node_to_del)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [node4])
        self.assertEqual(node2.Parent, None)
        # del root from tree
        root_to_del = SimpleTreeNode('a', None)
        tree.DeleteNode(root_to_del)
        self.assertEqual(tree.Root, None)

    def test_find_node(self):
        # find in empty
        tree = SimpleTree(None)
        self.assertEqual(tree.FindNodesByValue('a'), [])
        # find non-existing
        node1 = SimpleTreeNode('a', None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode('c', node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode('d', node1)
        tree.AddChild(node1, node4)
        self.assertEqual(tree.FindNodesByValue('e'), [])
        # find existing
        self.assertEqual(tree.FindNodesByValue('a')[0].NodeValue, 'a')
        self.assertEqual(len(tree.FindNodesByValue('a')), 1)
        # find several existing
        node5 = SimpleTreeNode('a', None)
        tree.AddChild(node4, node5)
        self.assertEqual(tree.FindNodesByValue('a'), [node1, node5])

    def test_move_node(self):
        # move from empty
        tree = SimpleTree(None)
        node1 = SimpleTreeNode('a', None)
        node2 = SimpleTreeNode('b', None)
        tree.MoveNode(node1, node2)
        self.assertEqual(tree.Root, None)
        tree.MoveNode(None, None)
        self.assertEqual(tree.Root, None)
        # move non-existing node
        non_existing_node = SimpleTreeNode('1', None)
        tree.AddChild(None, node1)
        tree.AddChild(node1, node2)
        tree.MoveNode(non_existing_node, node2)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [node2])
        self.assertEqual(node2.Parent, node1)
        self.assertEqual(node2.Children, [])
        # move to non-existing node
        node3 = SimpleTreeNode('c', node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode('d', node1)
        tree.AddChild(node1, node4)
        tree.MoveNode(non_existing_node, node2)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [node2, node4])
        self.assertEqual(node2.Parent, node1)
        self.assertEqual(node3.Parent, node2)
        self.assertEqual(node3.Children, [])
        self.assertEqual(node4.Parent, node1)
        self.assertEqual(node4.Children, [])
        # move root
        tree.MoveNode(node1, node2)
        self.assertEqual(tree.Root, node1)
        self.assertEqual(tree.Root.NodeValue, 'a')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Children, [node2, node4])
        self.assertEqual(node2.Parent, node1)
        self.assertEqual(node3.Parent, node2)
        self.assertEqual(node3.Children, [])
        self.assertEqual(node4.Parent, node1)
        self.assertEqual(node4.Children, [])
        # move to root
        tree.MoveNode(node3, node1)
        self.assertEqual(node2.Children, [])
        self.assertEqual(len(node1.Children), 3)
        self.assertEqual(node2 in node1.Children,True)
        self.assertEqual(node3 in node1.Children,True)
        self.assertEqual(node4 in node1.Children,True)
        # move existing
        node5 = SimpleTreeNode('e', None)
        tree.AddChild(node2, node5)
        node6 = SimpleTreeNode('f', None)
        tree.AddChild(node5, node6)
        tree.MoveNode(node5, node3)
        self.assertEqual(node2.Children, [])
        self.assertEqual(node3.Children, [node5])
        self.assertEqual(node5.Children, [node6])

    def test_count(self):
        # count empty
        tree = SimpleTree(None)
        self.assertEqual(tree.Count(), 0)
        # count non-empty
        node1 = SimpleTreeNode('a', None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode('c', node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode('d', node1)
        tree.AddChild(node1, node4)
        self.assertEqual(tree.Count(), 4)
        # count after deleting
        tree.DeleteNode(node3)
        self.assertEqual(tree.Count(), 3)

    def test_leaf_count(self):
        # leaf count empty
        tree = SimpleTree(None)
        self.assertEqual(tree.LeafCount(), 0)
        # leaf count non-empty
        node1 = SimpleTreeNode('a', None)
        tree.AddChild(None, node1)
        node2 = SimpleTreeNode('b', node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode('c', node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode('d', node1)
        tree.AddChild(node1, node4)
        self.assertEqual(tree.LeafCount(), 2)
        # leaf count after deleting
        tree.DeleteNode(node3)
        self.assertEqual(tree.LeafCount(), 2)
        # leaf count after moving
        tree.AddChild(node2, node3)
        tree.MoveNode(node3, node4)#
        self.assertEqual(tree.LeafCount(), 2)

if __name__ == '__main__':
    unittest.main()
