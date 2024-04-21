import unittest
from Graph import Vertex
from Graph import SimpleGraph


class TestBST(unittest.TestCase):
    
    def test_Add(self):
        graph = SimpleGraph(3)
        graph.AddVertex(1)

        self.assertEqual(graph.vertex[0].Value, 1)
        self.assertEqual(graph.vertex[1], None)
        self.assertEqual(graph.vertex[2], None)
        self.assertEqual(graph.IsEdge(1, 1), False)
        self.assertEqual(graph.IsEdge(0, 1), False)
        self.assertEqual(graph.IsEdge(1, 0), False)
        self.assertEqual(graph.IsEdge(2, 1), False)
        self.assertEqual(graph.IsEdge(1, 2), False)
        graph.AddEdge(1, 0)
        self.assertEqual(graph.IsEdge(0, 1), True)
        self.assertEqual(graph.IsEdge(1, 0), True)
        graph.RemoveEdge(1, 0)
        self.assertEqual(graph.IsEdge(0, 1), False)
        self.assertEqual(graph.IsEdge(1, 0), False)
        graph.AddEdge(1, 0)
        graph.AddEdge(1, 1)
        graph.AddEdge(0, 1)
        self.assertEqual(graph.IsEdge(1, 1), True)
        self.assertEqual(graph.IsEdge(0, 1), True)
        self.assertEqual(graph.IsEdge(1, 0), True)
        graph.RemoveVertex(1)
        self.assertEqual(graph.IsEdge(1, 1), False)
        self.assertEqual(graph.IsEdge(0, 1), False)
        self.assertEqual(graph.IsEdge(1, 0), False)


if __name__ == '__main__':
    unittest.main()