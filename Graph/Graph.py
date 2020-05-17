class Vertex:

    def __init__(self, val):
        self.Value = val

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = v
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
