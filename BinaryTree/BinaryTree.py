class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если в дереве вообще нету узлов
        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key, node=None, BSTFind_obj=None):
        # ищем в дереве узел и сопутствующую информацию по ключу
        if node is None:
            node = self.Root
            BSTFind_obj = BSTFind()
        if node:
            if key == node.NodeKey:
                BSTFind_obj.Node = node
                BSTFind_obj.NodeHasKey = True
                BSTFind_obj.ToLeft = False
            elif key < node.NodeKey:
                if node.LeftChild:
                    node = node.LeftChild
                    self.FindNodeByKey(key, node, BSTFind_obj)
                else:
                    BSTFind_obj.Node = node
                    BSTFind_obj.NodeHasKey = False
                    BSTFind_obj.ToLeft = True
            else:
                if node.RightChild:
                    node = node.RightChild
                    self.FindNodeByKey(key, node, BSTFind_obj)
                else:
                    BSTFind_obj.Node = node
                    BSTFind_obj.NodeHasKey = False
                    BSTFind_obj.ToLeft = False
            return BSTFind_obj
        else:
            return BSTFind_obj

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        BSTFind = self.FindNodeByKey(key)
        if BSTFind.Node:
            if BSTFind.NodeHasKey == True:
                return False # если ключ уже есть
            else:
                parent_node = BSTFind.Node
                node_add = BSTNode(key, val, parent_node)
                if BSTFind.ToLeft == True:
                    parent_node.LeftChild = node_add
                else:
                    parent_node.RightChild = node_add
        else:
            root = BSTNode(key, val, None)
            self.Root = root

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальное/минимальное (узел) в поддереве
        while not ((FromNode.LeftChild == None and FromNode.RightChild == None) or \
            (FromNode.LeftChild == None and FindMax == False) or \
            (FromNode.RightChild == None and FindMax == True)):
            if FindMax == True:
                FromNode = FromNode.RightChild
                self.FinMinMax(FromNode, FindMax)
            else:
                FromNode = FromNode.LeftChild
                self.FinMinMax(FromNode, FindMax)
        return FromNode

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        BSTFind = self.FindNodeByKey(key, node=None, BSTFind_obj=None)
        if BSTFind:
            if BSTFind.NodeHasKey == True:
                node_to_del = BSTFind.Node
                parent_node = node_to_del.Parent
                if node_to_del.LeftChild == None and node_to_del.RightChild == None:
                    if node_to_del != self.Root:
                        if parent_node.NodeKey <= node_to_del.NodeKey:
                            parent_node.RightChild = None
                            node_to_del.Parent = None
                        else:
                            parent_node.LeftChild = None
                            node_to_del.Parent = None
                    else:
                        self.Root = None
                elif node_to_del.LeftChild and node_to_del.RightChild == None:
                    if node_to_del != self.Root:
                        if parent_node.NodeKey <= node_to_del.NodeKey:
                            parent_node.RightChild = node_to_del.LeftChild
                            node_to_del.LeftChild.Parent = parent_node
                            node_to_del.Parent = None
                        else:
                            parent_node.LeftChild = node_to_del.LeftChild
                            node_to_del.LeftChild.Parent = parent_node
                            node_to_del.Parent = None
                    else:
                        node_to_del.LeftChild.Parent = None
                        self.Root = node_to_del.LeftChild
                elif node_to_del.LeftChild == None and node_to_del.RightChild:
                    if node_to_del != self.Root:
                        if parent_node.NodeKey <= node_to_del.NodeKey:
                            parent_node.RightChild = node_to_del.RightChild
                            node_to_del.LeftChild.Parent = parent_node
                            node_to_del.Parent = None
                        else:
                            parent_node.LeftChild = node_to_del.RightChild
                            node_to_del.LeftChild.Parent = parent_node
                            node_to_del.Parent = None
                    else:
                        node_to_del.RightChild.Parent = None
                        self.Root = node_to_del.RightChild
                else: # both are not None
                    min_node = self.FinMinMax(node_to_del.RightChild, FindMax=False)
                    if parent_node.NodeKey <= node_to_del.NodeKey:
                        if not min_node.Parent == node_to_del:
                            min_node.Parent.LeftChild = None
                            min_node.RightChild = node_to_del.RightChild
                            node_to_del.RightChild.Parent = min_node

                        if node_to_del != self.Root:
                            parent_node.RightChild = min_node
                            min_node.Parent = parent_node
                        else:
                            min_node.Parent = None
                            self.Root = min_node

                        node_to_del.LeftChild.Parent = min_node
                        min_node.LeftChild = node_to_del.LeftChild

                        node_to_del.Parent = None
                    else:
                        if not min_node.Parent == node_to_del:
                            min_node.Parent.LeftChild = None
                            min_node.RightChild = node_to_del.RightChild
                            node_to_del.RightChild.Parent = min_node

                        if node_to_del != self.Root:
                            parent_node.LeftChild = min_node
                            min_node.Parent = parent_node
                        else:
                            min_node.Parent = None
                            self.Root = min_node

                        node_to_del.LeftChild.Parent = min_node
                        min_node.LeftChild = node_to_del.LeftChild

                        node_to_del.Parent = None
            else:
                return False
        else:
            return False # если узел не найден

    def Count(self, level=[], all_nodes=[]):
        if not level:
            level.append(self.Root)
            all_nodes=[]
            all_nodes.append(self.Root)
        for node in level:
            new_level = []
            if node:
                left_child = node.LeftChild
                if left_child:
                    new_level.append(left_child)
                else:
                    pass
                right_child = node.RightChild
                if right_child:
                    new_level.append(right_child)
                else:
                    pass
            else:
                pass
        if new_level:
            all_nodes.extend(new_level)
            self.Count(new_level, all_nodes)
        return len(all_nodes) # количество узлов в дереве
