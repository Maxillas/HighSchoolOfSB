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

    def test_DepthFirstSearch(self):
        graph = SimpleGraph(3)
        graph.AddVertex(0)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddEdge(1, 2)

        # self.assertEqual(graph.DepthFirstSearch(0, 1), [])
        #
        # graph.AddEdge(0, 1)
        # self.assertEqual(graph.DepthFirstSearch(0, 1)[0].Value, 0)
        # self.assertEqual(graph.DepthFirstSearch(0, 1)[1].Value, 1)
        #
        # self.assertEqual(graph.DepthFirstSearch(0, 2)[0].Value, 0)
        # self.assertEqual(graph.DepthFirstSearch(0, 2)[1].Value, 1)
        # self.assertEqual(graph.DepthFirstSearch(0, 2)[2].Value, 2)
        #
        # self.assertEqual(graph.DepthFirstSearch(1, 2)[0].Value, 1)
        # self.assertEqual(graph.DepthFirstSearch(1, 2)[1].Value, 2)


    def test_DepthFirstSearch2(self):
        graph = SimpleGraph(11)
        graph.AddVertex(0)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddVertex(4)
        graph.AddVertex(5)
        graph.AddVertex(6)
        graph.AddVertex(7)
        graph.AddVertex(8)
        graph.AddVertex(9)
        graph.AddVertex(10)
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(4, 5)
        graph.AddEdge(5, 6)
        graph.AddEdge(2, 6)
        graph.AddEdge(2, 7)
        graph.AddEdge(3, 8)
        graph.AddEdge(3, 9)
        graph.AddEdge(5, 9)
        graph.AddEdge(1, 3)

        # self.assertEqual(graph.DepthFirstSearch(0, 6)[0].Value, 0)
        # self.assertEqual(graph.DepthFirstSearch(0, 6)[1].Value, 1)
        # self.assertEqual(graph.DepthFirstSearch(0, 6)[2].Value, 2)
        # self.assertEqual(graph.DepthFirstSearch(0, 6)[3].Value, 6)
        #
        # self.assertEqual(graph.DepthFirstSearch(0, 2)[0].Value, 0)
        # self.assertEqual(graph.DepthFirstSearch(0, 2)[1].Value, 1)
        # self.assertEqual(graph.DepthFirstSearch(0, 2)[2].Value, 2)
        #
        # self.assertEqual(len(graph.DepthFirstSearch(3, 7)), 5)
        # self.assertEqual(graph.DepthFirstSearch(3, 7)[0].Value, 3)
        # self.assertEqual(graph.DepthFirstSearch(3, 7)[1].Value, 0)
        # self.assertEqual(graph.DepthFirstSearch(3, 7)[2].Value, 1)
        # self.assertEqual(graph.DepthFirstSearch(3, 7)[3].Value, 2)
        # self.assertEqual(graph.DepthFirstSearch(3, 7)[4].Value, 7)

    def test_DepthFirstSearch(self):
        graph = SimpleGraph(3)
        graph.AddVertex(0)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddEdge(1, 2)

        self.assertEqual(graph.BreadthFirstSearch(0, 1), [])

        graph.AddEdge(0, 1)
        self.assertEqual(graph.BreadthFirstSearch(0, 1)[0], 0)
        self.assertEqual(graph.BreadthFirstSearch(0, 1)[1], 1)

        self.assertEqual(graph.BreadthFirstSearch(0, 2)[0], 0)
        self.assertEqual(graph.BreadthFirstSearch(0, 2)[1], 1)
        self.assertEqual(graph.BreadthFirstSearch(0, 2)[2], 2)

        self.assertEqual(graph.BreadthFirstSearch(1, 2)[0], 1)
        self.assertEqual(graph.BreadthFirstSearch(1, 2)[1], 2)

if __name__ == '__main__':
    unittest.main()