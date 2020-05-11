class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла

class BalancedBST:

    def __init__(self):
    	self.Root = None # корень дерева

    def GenerateTree(self, a):
        # создаём дерево с нуля из неотсортированного массива a
        sorted_array = sorted(a)
        self.build_BST(sorted_array)

    def build_BST(self, sorted_array, parent=None, level=0):
        if sorted_array == []:
            pass
        else:
            level += 1
            if len(sorted_array) % 2 == 0:
                mid = int(len(sorted_array) / 2 - 1)
            else:
                mid = int(len(sorted_array) / 2)
            node = BSTNode(sorted_array[mid], parent)
            if node.Parent is None:
                self.Root = node
            node.Level = level
            node.LeftChild = self.build_BST(sorted_array[:mid], node, level)
            node.RightChild = self.build_BST(sorted_array[mid + 1:], node, level)
            return node

    def IsBalanced(self, root_node=None):
        if root_node is None:
            root_node = self.Root

        if root_node is None:
            return False

        inorder_traversed_list = self.inorder_traverse_level(root_node)
        return self.is_balanced(inorder_traversed_list)

    def inorder_traverse_level(self, node):
        if node is None:
            return []
        return (self.inorder_traverse_level(node.LeftChild) + \
                [node.Level]) + \
                self.inorder_traverse_level(node.RightChild)

    def is_balanced(self, array, level=1):
        index = array.index(level)
        if not index:
            pass
        else:
            max_left = max(array[:index])
            max_right = max(array[index+1:])
            if abs(max_left - max_right) > 1:
                return False
            else:
                level += 1
                self.is_balanced(array[:index], level)
                self.is_balanced(array[index+1:], level)
            return True
