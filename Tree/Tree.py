class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if ParentNode: # not None:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)
        else: # NewChild => root
            self.Root = NewChild
            NewChild.Parent = None

    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete
        if self.Root:
            if self.Root.NodeValue == NodeToDelete.NodeValue:
                self.Root = None
            else:
                all_nodes = self.GetAllNodes()
                for node in all_nodes:
                    if node.NodeValue == NodeToDelete.NodeValue:
                        parentNode = node.Parent
                        parentNode.Children.remove(node)
                        node.Parent = None
        else:
            pass

    def GetAllNodes(self, node = None, all_nodes = []):
        # ваш код выдачи всех узлов дерева в определённом порядке
        if node is None:
            node = self.Root
            all_nodes = [node]
        if node:
            for child in node.Children:
                if child not in all_nodes:
                    all_nodes.append(child)
                self.GetAllNodes(child, all_nodes)
            return all_nodes
        else:
            return all_nodes

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        nodes_found = []
        if self.Root:
            all_nodes = self.GetAllNodes()
            for node in all_nodes:
                if node.NodeValue == val:
                    nodes_found.append(node)
                else:
                    pass
            return nodes_found
        else:
            return nodes_found

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        all_nodes = self.GetAllNodes()
        if OriginalNode in all_nodes and NewParent in all_nodes:
            if OriginalNode == self.Root:
                pass
            else:
                for node in all_nodes:
                    if node.NodeValue == OriginalNode.NodeValue:
                        oldParent = node.Parent
                        oldParent.Children.remove(node)
                        NewParent.Children.append(node)
                        node.Parent = NewParent
        else:
            pass

    def Count(self):
        # количество всех узлов в дереве
        if self.Root:
            all_nodes = self.GetAllNodes()
            return len(all_nodes)
        else:
            return 0

    def LeafCount(self):
        # количество листьев в дереве
        if not self.Root:
            return 0
        else:
            all_nodes = self.GetAllNodes()
            leafs = []
            for node in all_nodes:
                if node.Children:
                    pass
                else:
                    leafs.append(node)
            return len(leafs)

    def define_level(self):
        pass
