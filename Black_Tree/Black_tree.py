class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
        self.Level = None

class SimpleTree:

    def __init__(self, root):
        if root is not None:
            self.Root = root # корень, может быть None
            root.Level = 0
        else:
            self.Root = root

    def AddChild(self, ParentNode, NewChild):
        if ParentNode: # not None:
            NewChild.Parent = ParentNode
            NewChild.Level = NewChild.Parent.Level + 1
            ParentNode.Children.append(NewChild)
        else: # NewChild => root
            self.Root = NewChild
            NewChild.Level = 0
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

    def getLeafs(self):
        # количество листьев в дереве
        if not self.Root:
            return []
        else:
            all_nodes = self.GetAllNodes()
            leafs = []
            for node in all_nodes:
                if node.Children:
                    pass
                else:
                    if leafs == []:
                        leafs.append(node)
                    else:
                        for i in range(len(leafs)):
                            if node.Level > leafs[i].Level:
                                leafs.insert(i, node)
                                break
                            else:
                                pass
                        if node not in leafs:
                            leafs.append(node)
            return leafs

    def LeafCount(self):
        # количество листьев в дереве
        leafs = self.getLeafs()
        return len(leafs)

    def EvenTrees(self, leafs=None, nodes_to_remove=[], used_nodes=[]):
        if leafs is None:
            leafs = self.getLeafs()
            nodes_to_remove = []
            used_nodes=[]
        if leafs == []:
            return nodes_to_remove
        else:
            new_leafs = []
            for leaf in leafs:
                if leaf in used_nodes:
                    pass
                else:
                    # print(leaf.NodeValue)
                    if leaf == self.Root:
                        pass
                    else:
                        parent = leaf.Parent
                        if parent == self.Root:
                            pass
                        else:
                            if len(set(parent.Children) - set(used_nodes)) >= 2:
                                parent_of_parent = parent.Parent
                                for child in parent.Children:
                                    used_nodes.append(child)
                                if parent_of_parent == self.Root:
                                    if len(parent.Children) % 2 != 0 and \
                                        len(parent_of_parent.Children) > 1:
                                        nodes_to_remove.append(parent_of_parent)
                                        nodes_to_remove.append(parent)
                                    else:
                                        pass
                                else:
                                    nodes_to_remove.append(parent_of_parent.Parent)
                                    nodes_to_remove.append(parent_of_parent)
                                    if parent_of_parent.Parent != self.Root and \
                                        parent_of_parent.Parent not in new_leafs:
                                        new_leafs.append(parent_of_parent.Parent)
                            else:
                                if parent.Parent == self.Root:
                                    if len(parent.Parent.Children) < 2:
                                        pass
                                    else:
                                        nodes_to_remove.append(parent.Parent)
                                        nodes_to_remove.append(parent)
                                else:
                                    nodes_to_remove.append(parent.Parent)
                                    nodes_to_remove.append(parent)
                                    if len(parent.Parent.Children) < 2:
                                        if parent.Parent not in new_leafs:
                                            new_leafs.append(parent.Parent)
                                        else:
                                            pass
                                    else:
                                        used_nodes.append(parent)
        if new_leafs != []:
            self.EvenTrees(new_leafs, nodes_to_remove, used_nodes)
        return nodes_to_remove
