import unittest
from BinarySimpleTree import BSTNode
from BinarySimpleTree import BST


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
        tree = BST(None)

        result = tree.FindNodeByKey(15)

        self.assertEqual(result.Node, None)
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

        tree.AddKeyValue(node1.NodeKey, node1.NodeValue)
        tree.AddKeyValue(node2.NodeKey, node2.NodeValue)

        self.assertEqual(tree.FindNodeByKey(node1.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.FindNodeByKey(node2.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.Root.LeftChild.NodeValue, 15)
        self.assertEqual(tree.Root.RightChild.NodeValue, 20)

        tree.AddKeyValue(node2.NodeKey, node2.NodeValue)

        self.assertEqual(tree.FindNodeByKey(node1.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.FindNodeByKey(node2.NodeKey).NodeHasKey, True)
        self.assertEqual(tree.Root.LeftChild.NodeValue, 15)
        self.assertEqual(tree.Root.RightChild.NodeValue, 20)

    def test_FinMinMax(self):
        nodeRoot = BSTNode(16, 16, None)
        node1 = BSTNode(15, 15, None)
        node2 = BSTNode(20, 20, None)
        node3 = BSTNode(30, 30, None)
        node4 = BSTNode(18, 18, None)
        node5 = BSTNode(7, 7, None)
        tree = BST(nodeRoot)

        tree.AddKeyValue(node1.NodeKey, node1.NodeValue)
        tree.AddKeyValue(node2.NodeKey, node2.NodeValue)
        tree.AddKeyValue(node3.NodeKey, node3.NodeValue)
        tree.AddKeyValue(node4.NodeKey, node4.NodeValue)
        tree.AddKeyValue(node5.NodeKey, node5.NodeValue)

        self.assertEqual(tree.Root.LeftChild.LeftChild.NodeValue, 7)

        self.assertEqual(tree.FinMinMax(nodeRoot, True).NodeValue, 30)
        self.assertEqual(tree.FinMinMax(nodeRoot, False).NodeValue, 7)
        self.assertEqual(tree.FinMinMax(tree.Root.LeftChild, True).NodeValue, 15)
        self.assertEqual(tree.FinMinMax(tree.Root.LeftChild, False).NodeValue, 7)
        self.assertEqual(tree.FinMinMax(tree.Root.RightChild, True).NodeValue, 30)
        self.assertEqual(tree.FinMinMax(tree.Root.RightChild, False).NodeValue, 18)

    def test_DeleteNodeByKey(self):
        nodeRoot = BSTNode(16, 16, None)
        node1 = BSTNode(15, 15, None)
        node2 = BSTNode(20, 20, None)
        node3 = BSTNode(30, 30, None)
        node4 = BSTNode(18, 18, None)
        node5 = BSTNode(7, 7, None)
        tree = BST(nodeRoot)

        tree.AddKeyValue(node1.NodeKey, node1.NodeValue)
        tree.AddKeyValue(node2.NodeKey, node2.NodeValue)
        tree.AddKeyValue(node3.NodeKey, node3.NodeValue)
        tree.AddKeyValue(node4.NodeKey, node4.NodeValue)
        tree.AddKeyValue(node5.NodeKey, node5.NodeValue)

        self.assertEqual(nodeRoot.RightChild.NodeValue, 20)
        self.assertEqual(nodeRoot.RightChild.RightChild.NodeValue, 30)
        self.assertEqual(tree.Count(), 6)

        tree.DeleteNodeByKey(20)

        self.assertEqual(nodeRoot.RightChild.NodeValue, 30)
        self.assertEqual(nodeRoot.RightChild.LeftChild.NodeValue, 18)
        self.assertEqual(tree.Count(), 5)

    def test_DeleteNodeByKeyRoot(self):
        nodeRoot = BSTNode(10, 10, None)
        node1 = BSTNode(15, 15, None)
        node2 = BSTNode(13, 13, None)
        tree = BST(nodeRoot)

        tree.AddKeyValue(node1.NodeKey, node1.NodeValue)
        tree.AddKeyValue(node2.NodeKey, node2.NodeValue)

        self.assertEqual(nodeRoot.RightChild.NodeValue, node1.NodeValue)
        self.assertEqual(nodeRoot.RightChild.LeftChild.NodeValue, node2.NodeValue)


        self.assertEqual(tree.Count(), 3)

        tree.DeleteNodeByKey(10)


