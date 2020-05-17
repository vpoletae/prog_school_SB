import unittest
from Graph import *

class Test_Graph(unittest.TestCase):

    def test_add_vertex(self):
        graph_empty =SimpleGraph(0)
        graph_empty.AddVertex(1)
        self.assertEqual(graph_empty.vertex, [])
        graph = SimpleGraph(3)
        graph.AddVertex(1)
        self.assertEqual(graph.vertex[0].Value, 1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        self.assertEqual(graph.vertex[0].Value, 1)
        self.assertEqual(graph.vertex[1].Value, 2)
        self.assertEqual(graph.vertex[2].Value, 3)
        graph.AddVertex(4)
        self.assertEqual(graph.max_vertex, 3)
        self.assertEqual(graph.vertex[0].Value, 1)
        self.assertEqual(graph.vertex[1].Value, 2)
        self.assertEqual(graph.vertex[2].Value, 3)

    def test_remove_vertex_with_no_edges(self):
        graph = SimpleGraph(3)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.RemoveVertex(0)
        self.assertEqual(graph.vertex[0], None)
        graph.RemoveVertex(1)
        self.assertEqual(graph.vertex[1], None)
        graph.RemoveVertex(2)
        self.assertEqual(graph.vertex[2], None)

    def test_remove_vertex_with_no_edges(self):
        graph = SimpleGraph(3)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddEdge(0, 1)
        self.assertEqual(graph.IsEdge(0, 1), True)
        graph.AddEdge(0, 2)
        self.assertEqual(graph.IsEdge(0, 2), True)
        self.assertEqual(graph.IsEdge(1, 2), False)
        graph.RemoveVertex(0)
        self.assertEqual(graph.IsEdge(0, 1), False)
        self.assertEqual(graph.IsEdge(0, 2), False)
        self.assertEqual(graph.m_adjacency[0], [0, 0, 0])
        self.assertEqual(graph.m_adjacency[1], [0, 0, 0])
        self.assertEqual(graph.m_adjacency[2], [0, 0, 0])

    def test_remove_vertex_with_no_edges(self):
        graph = SimpleGraph(3)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddEdge(0, 1)
        self.assertEqual(graph.IsEdge(0, 1), True)
        graph.RemoveEdge(0, 1)
        self.assertEqual(graph.IsEdge(0, 1), False)
        self.assertEqual(graph.m_adjacency[0], [0, 0, 0])
        self.assertEqual(graph.m_adjacency[1], [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
