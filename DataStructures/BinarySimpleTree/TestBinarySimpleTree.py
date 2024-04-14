import unittest
from SimpleTree import SimpleTree
from SimpleTree import SimpleTreeNode


class TestBST(unittest.TestCase):

    def test_FindNodeByKey(self):
        nodeRoot = BSTNode(16, 16, None)
        node1 = BSTNode(15, 15, None)
        node2 = BSTNode(20, 20, None)
        node3 = BSTNode(30, 30, None)
        tree = BST(nodeRoot)

        result = tree.FindNodeByKey(15)

        self.assertEqual(result.Node, nodeRoot)
        self.assertEqual(result.NodeHasKey, False)
        self.assertEqual(result.ToLeft, True)

        result = tree.FindNodeByKey(18)

        self.assertEqual(result.Node, nodeRoot)
        self.assertEqual(result.NodeHasKey, False)
        self.assertEqual(result.ToLeft, False)

        result = tree.FindNodeByKey(16)

        self.assertEqual(result.Node, nodeRoot)
        self.assertEqual(result.NodeHasKey, True)
        self.assertEqual(result.ToLeft, False)

    def test_FindNodeByKeyEmptyNode(self):
        tree = BST()

        result = tree.FindNodeByKey(15)

        self.assertEqual(result.Node, False)
        self.assertEqual(result.NodeHasKey, False)
        self.assertEqual(result.ToLeft, False)

    def test_AddKeyValue(self):
        nodeRoot = BSTNode(16, 16, None)
        node1 = BSTNode(15, 15, None)
        node2 = BSTNode(20, 20, None)
        node3 = BSTNode(30, 30, None)
        tree = BST(nodeRoot)

        self.assertEqual(tree.FindNodeByKey(node1.NodeKey).NodeHasKey, False)
        self.assertEqual(tree.FindNodeByKey(node2.NodeKey).NodeHasKey, False)

        tree.AddKeyValue(node1.NodeKey)
        tree.AddKeyValue(node2.NodeKey)

        self.assertEqual(tree.FindNodeByKey(node1.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.FindNodeByKey(node2.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.Root.LeftChild, node1)
        self.assertEqual(tree.Root.RightChild, node2)

        tree.AddKeyValue(node2.NodeKey)

        self.assertEqual(tree.FindNodeByKey(node1.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.FindNodeByKey(node2.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.Root.LeftChild, node1)
        self.assertEqual(tree.Root.RightChild, node2)

    def test_FinMinMax(self):
        nodeRoot = BSTNode(16, 16, None)
        node1 = BSTNode(15, 15, None)
        node2 = BSTNode(20, 20, None)
        node3 = BSTNode(30, 30, None)
        node4 = BSTNode(18, 18, None)
        node5 = BSTNode(7, 7, None)
        tree = BST(nodeRoot)

        tree.AddKeyValue(node1.NodeKey)
        tree.AddKeyValue(node2.NodeKey)
        tree.AddKeyValue(node3.NodeKey)
        tree.AddKeyValue(node4.NodeKey)
        tree.AddKeyValue(node5.NodeKey)

        self.assertEqual(tree.FinMinMax(nodeRoot, True), 30)
        self.assertEqual(tree.FinMinMax(nodeRoot, False), 7)
        self.assertEqual(tree.FinMinMax(node1, True), 15)
        self.assertEqual(tree.FinMinMax(node1, False), 7)
        self.assertEqual(tree.FinMinMax(node2, True), 30)
        self.assertEqual(tree.FinMinMax(node2, False), 18)

    def test_DeleteNodeByKey(self):
        nodeRoot = BSTNode(16, 16, None)
        node1 = BSTNode(15, 15, None)
        node2 = BSTNode(20, 20, None)
        node3 = BSTNode(30, 30, None)
        node4 = BSTNode(18, 18, None)
        node5 = BSTNode(7, 7, None)
        tree = BST(nodeRoot)

        tree.AddKeyValue(node1.NodeKey)
        tree.AddKeyValue(node2.NodeKey)
        tree.AddKeyValue(node3.NodeKey)
        tree.AddKeyValue(node4.NodeKey)
        tree.AddKeyValue(node5.NodeKey)

        self.assertEqual(nodeRoot.RightChild, node2)
        self.assertEqual(tree.Count, 6)

        tree.DeleteNodeByKey(20)

        self.assertEqual(nodeRoot.RightChild, node3)
        self.assertEqual(node3.LeftChild, node4)
        self.assertEqual(tree.Count, 5)
