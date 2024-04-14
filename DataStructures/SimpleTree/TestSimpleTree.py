import unittest
from SimpleTree import SimpleTree
from SimpleTree import SimpleTreeNode


class TestBloomFilter(unittest.TestCase):

    def test_AddChild1(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root, node3)

        self.assertEqual(tree.Root.NodeValue, 10)
        self.assertEqual(tree.Root.Children[0].NodeValue, 15)
        self.assertEqual(tree.Root.Children[1].NodeValue, 20)
        self.assertEqual(tree.Root.Children[2].NodeValue, 30)

        self.assertEqual(tree.Root.Children[0].Parent, tree.Root)
        self.assertEqual(tree.Root.Children[1].Parent, tree.Root)
        self.assertEqual(tree.Root.Children[2].Parent, tree.Root)

    def test_AddChild2(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root.Children[0], node2)
        tree.AddChild(tree.Root.Children[0].Children[0], node3)

        self.assertEqual(tree.Root.NodeValue, 10)
        self.assertEqual(tree.Root.Children[0].NodeValue, 15)
        self.assertEqual(tree.Root.Children[0].Children[0].NodeValue, 20)
        self.assertEqual(tree.Root.Children[0].Children[0].Children[0].NodeValue, 30)

    def test_Delete1(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root, node3)

        tree.DeleteNode(node1)

        self.assertEqual(tree.Root.NodeValue, 10)
        self.assertEqual(tree.Root.Children[0], node2)
        self.assertEqual(tree.Root.Children[1], node3)

        self.assertEqual(node1.Parent, None)
        self.assertEqual(len(node1.Children), 0)

        tree.DeleteNode(nodeRoot)

        self.assertEqual(tree.Root.NodeValue, 10)
        self.assertEqual(tree.Root.Children[0], node2)
        self.assertEqual(tree.Root.Children[1], node3)

        self.assertEqual(node1.Parent, None)
        self.assertEqual(len(node1.Children), 0)

    def test_Delete2(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root.Children[0], node2)
        tree.AddChild(tree.Root.Children[0].Children[0], node3)

        self.assertEqual(len(tree.Root.Children), 1)

        tree.DeleteNode(node1)

        self.assertEqual(tree.Root, nodeRoot)
        self.assertEqual(len(tree.Root.Children), 0)
        self.assertEqual(node1.Parent, None)
        self.assertEqual(len(node1.Children), 0)

    def test_getAllNodes1(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root.Children[0], node2)
        tree.AddChild(tree.Root.Children[0].Children[0], node3)

        expectedNodeList = [nodeRoot, node1, node2, node3]
        self.assertEqual(tree.GetAllNodes(), expectedNodeList)

    def test_getAllNodes2(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        node4 = SimpleTreeNode(25, None)
        node5 = SimpleTreeNode(26, None)
        node6 = SimpleTreeNode(27, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root.Children[1], node4)
        tree.AddChild(tree.Root.Children[1], node5)
        tree.AddChild(tree.Root.Children[1], node6)
        tree.AddChild(tree.Root, node3)

        expectedNodeList = [nodeRoot, node1, node2, node4, node5, node6, node3]
        self.assertEqual(tree.GetAllNodes(), expectedNodeList)

    def test_findNodesByValue(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(10, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        node4 = SimpleTreeNode(25, None)
        node5 = SimpleTreeNode(20, None)
        node6 = SimpleTreeNode(20, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root.Children[1], node4)
        tree.AddChild(tree.Root.Children[1], node5)
        tree.AddChild(tree.Root.Children[1], node6)
        tree.AddChild(tree.Root, node3)

        self.assertEqual(len(tree.FindNodesByValue(20)), 3)
        self.assertEqual(len(tree.FindNodesByValue(10)), 2)
        self.assertEqual(len(tree.FindNodesByValue(30)), 1)
        self.assertEqual(len(tree.FindNodesByValue(25)), 1)

    def test_moveNode(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        node4 = SimpleTreeNode(25, None)
        node5 = SimpleTreeNode(20, None)
        node6 = SimpleTreeNode(20, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root.Children[1], node4)
        tree.AddChild(tree.Root.Children[1], node5)
        tree.AddChild(tree.Root.Children[1], node6)
        tree.AddChild(tree.Root, node3)

        tree.MoveNode(node2, node1)

        self.assertEqual(len(tree.Root.Children), 2)
        self.assertEqual(tree.Root.Children[0], node1)
        self.assertEqual(tree.Root.Children[1], node3)
        self.assertEqual(node1.Children[0], node2)
        self.assertEqual(len(node2.Children), 3)

    def test_count(self):
        nodeRoot = SimpleTreeNode(10, None)
        node1 = SimpleTreeNode(15, None)
        node2 = SimpleTreeNode(20, None)
        node3 = SimpleTreeNode(30, None)
        node4 = SimpleTreeNode(25, None)
        node5 = SimpleTreeNode(20, None)
        node6 = SimpleTreeNode(20, None)
        tree = SimpleTree(nodeRoot)

        tree.AddChild(tree.Root, node1)
        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root.Children[1], node4)
        tree.AddChild(tree.Root.Children[1], node5)
        tree.AddChild(tree.Root.Children[1], node6)
        tree.AddChild(tree.Root, node3)

        self.assertEqual(tree.Count(), 7)
        self.assertEqual(tree.LeafCount(), 5)