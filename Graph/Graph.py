class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        vertex = Vertex(v)
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = vertex
                break
            else:
                pass

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        assert v <= self.max_vertex-1
        self.vertex[v] = None
        for i in range(self.max_vertex):
            if i == v:
                pass
            else:
                self.RemoveEdge(v, i)
        self.m_adjacency[v] = [0] * self.max_vertex

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.m_adjacency[v1][v2] == 1:
            return True
        else:
            return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if self.m_adjacency[v1][v2] == 1:
            pass
        else:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if self.m_adjacency[v1][v2] == 0:
            pass
        else:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo, stack=None, trigger=0):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if trigger == 0:
            stack = []
            for vertex in self.vertex:
                vertex.Hit = False
            trigger = 1
        vertex = self.vertex[VFrom]
        vertex.Hit = True
        if vertex not in stack:
            stack.append(vertex)
        adj_list = self.m_adjacency[VFrom]
        if adj_list[VTo] == 1: #adjust
            stack.append(self.vertex[VTo])
        else:
            # get list of adjacent vertex indeces
            adj_vertex = []
            for i in range(len(adj_list)):
                if adj_list[i] == 1:
                    if self.vertex[i].Hit == False:
                        adj_vertex.append(i)
                    else: pass
                else: pass

            if adj_vertex != []:
                for index in adj_vertex:
                    self.DepthFirstSearch(index, VTo, stack, trigger)
            else:
                stack.pop(-1)
                if stack == []:
                    pass
                else:
                    index = self.vertex.index(stack[-1])
                    self.DepthFirstSearch(index, VTo, stack, trigger)
        return stack
