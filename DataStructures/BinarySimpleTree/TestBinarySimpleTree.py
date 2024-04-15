import unittest
from BinarySimpleTree import BSTNode
from BinarySimpleTree import BSTFind
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

    def test_node(self):
        node = BSTNode(key=1, val=1, parent=None)
        self.assertIsInstance(node, BSTNode)
        self.assertEqual(node.NodeKey, 1)
        self.assertEqual(node.NodeValue, 1)
        self.assertIsNone(node.Parent)

    def test_find_node(self):
        tree = BST(None)
        # нет ни одного узла
        search_result = tree.FindNodeByKey(1)
        self.assertIsInstance(search_result, BSTFind)
        self.assertIsNone(search_result.Node)
        self.assertFalse(search_result.ToLeft)
        self.assertFalse(search_result.NodeHasKey)
        # добавили корень
        tree.AddKeyValue(10, 1)
        self.assertEqual(tree.Root.NodeKey, 10)
        # запрошенный ключ добавляем левому потомку
        search_result = tree.FindNodeByKey(8)
        self.assertEqual(search_result.Node.NodeKey, 10)
        self.assertTrue(search_result.ToLeft)
        self.assertFalse(search_result.NodeHasKey)
        # запрошенный ключ добавляем правому потомку
        search_result = tree.FindNodeByKey(12)
        self.assertEqual(search_result.Node.NodeKey, 10)
        self.assertFalse(search_result.ToLeft)
        self.assertFalse(search_result.NodeHasKey)
        tree.AddKeyValue(8, 1)
        # проверяем поиск присутствующего ключа
        search_result = tree.FindNodeByKey(8)
        self.assertEqual(search_result.Node.NodeKey, 8)
        self.assertFalse(search_result.ToLeft)
        self.assertTrue(search_result.NodeHasKey)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 8)

    def test_add_root_node(self):
        tree = BST(None)
        self.assertIsNone(tree.FindNodeByKey(10).Node)
        self.assertTrue(tree.AddKeyValue(10, 1))
        self.assertIsNotNone(tree.FindNodeByKey(10).Node)
        self.assertIsInstance(tree.Root, BSTNode)
        self.assertEqual(tree.Root.NodeKey, 10)
        self.assertEqual(tree.Root.NodeValue, 1)
        self.assertIsNone(tree.Root.Parent)
        self.assertIsNone(tree.Root.LeftChild)
        self.assertIsNone(tree.Root.RightChild)

    def test_add_many_nodes(self):
        tree = BST(None)
        self.assertIsNone(tree.FindNodeByKey(10).Node)
        self.assertIsNone(tree.FindNodeByKey(8).Node)
        self.assertIsNone(tree.FindNodeByKey(12).Node)
        self.assertTrue(tree.AddKeyValue(10, 1))
        self.assertTrue(tree.AddKeyValue(8, 2))
        self.assertTrue(tree.AddKeyValue(12, 3))
        self.assertIsNotNone(tree.FindNodeByKey(10).Node)
        self.assertIsNotNone(tree.FindNodeByKey(8).Node)
        self.assertIsNotNone(tree.FindNodeByKey(12).Node)
        self.assertIsNone(tree.Root.Parent)
        self.assertIsInstance(tree.Root.LeftChild, BSTNode)
        self.assertIsInstance(tree.Root.RightChild, BSTNode)
        self.assertLess(
            tree.Root.LeftChild.NodeKey, tree.Root.NodeKey
        )
        self.assertGreater(
            tree.Root.RightChild.NodeKey, tree.Root.NodeKey
        )
        self.assertEqual(
            tree.Root.LeftChild.Parent.NodeKey, tree.Root.NodeKey
        )
        self.assertEqual(
            tree.Root.RightChild.Parent.NodeKey, tree.Root.NodeKey
        )
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


    def test_DeleteNodeByKeyRoot2(self):
        nodeRoot = BSTNode(10, 10, None)
        tree = BST(nodeRoot)

        tree.AddKeyValue(8, 8)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(7, 7)

        self.assertEqual(tree.Root.NodeValue, 10)
        self.assertEqual(tree.Root.RightChild, None)
        self.assertEqual(tree.Root.LeftChild.NodeValue, 8)
        self.assertEqual(tree.Root.LeftChild.LeftChild.NodeValue, 7)
        self.assertEqual(tree.Root.LeftChild.RightChild.NodeValue, 9)

        self.assertEqual(tree.Count(), 4)

        tree.DeleteNodeByKey(10)

        self.assertEqual(tree.Root.NodeValue, 8)
        self.assertEqual(tree.Root.RightChild.NodeValue, 9)
        self.assertEqual(tree.Root.LeftChild.NodeValue, 7)
        self.assertEqual(tree.Root.Parent, None)

    def test_delete_last_node(self):
        tree = BST(None)
        tree.AddKeyValue(10, 1)
        tree.AddKeyValue(8, 2)
        tree.AddKeyValue(12, 3)
        tree.AddKeyValue(11, 3)

        self.assertTrue(tree.DeleteNodeByKey(11))
        self.assertEqual(tree.Root.LeftChild.NodeKey, 8)
        self.assertEqual(tree.Root.RightChild.NodeKey, 12)
        self.assertIsNone(tree.Root.RightChild.RightChild)
        self.assertIsNone(tree.Root.RightChild.LeftChild)
        self.assertEqual(tree.Count(), 3)


    def test_delete_root(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertEqual(tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 50)
        self.assertTrue(tree.DeleteNodeByKey(50))
        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(tree.Root.NodeKey, 75)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 75)
        self.assertIsNone(tree.Root.RightChild)

    def test_delete_root_with_right_child(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertEqual(tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 50)
        # добавляем правого потомка для преемника
        tree.AddKeyValue(100, 3)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 100)
        self.assertEqual(
            tree.Root.RightChild.RightChild.Parent.NodeKey, 75
        )
        self.assertTrue(tree.DeleteNodeByKey(50))
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.NodeKey, 75)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 75)
        self.assertEqual(tree.Root.RightChild.NodeKey, 100)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 75)
        self.assertIsNone(tree.Root.RightChild.LeftChild)
        self.assertIsNone(tree.Root.RightChild.RightChild)

    def test_delete_root_and_node_successor_is_leaf(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(60, 3)
        self.assertTrue(tree.DeleteNodeByKey(50))
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.NodeKey, 60)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 60)
        self.assertEqual(tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 60)
        self.assertIsNone(tree.Root.RightChild.LeftChild)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 100)
        self.assertEqual(
            tree.Root.RightChild.RightChild.Parent.NodeKey, 75
        )

    def test_delete_root_and_node_successor_is_not_leaf(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 3)
        self.assertTrue(tree.DeleteNodeByKey(50))
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.NodeKey, 60)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 60)
        self.assertEqual(tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 60)
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey, 65)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 100)
        self.assertIsNone(tree.Root.RightChild.RightChild.RightChild)
        self.assertIsNone(tree.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(tree.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(tree.Root.RightChild.LeftChild.LeftChild)
        self.assertEqual(
            tree.Root.RightChild.RightChild.Parent.NodeKey, 75
        )
        self.assertEqual(
            tree.Root.RightChild.LeftChild.Parent.NodeKey, 75
        )

    def test_node_successor_parent_is_node_delete_leaf(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 3)
        self.assertTrue(tree.DeleteNodeByKey(75))
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.NodeKey, 50)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(tree.Root.RightChild.NodeKey, 100)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 50)
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey, 60)
        self.assertIsNone(tree.Root.RightChild.RightChild)
        self.assertEqual(
            tree.Root.RightChild.LeftChild.RightChild.NodeKey, 65
        )
        self.assertIsNone(tree.Root.RightChild.LeftChild.LeftChild)
        self.assertEqual(
            tree.Root.RightChild.LeftChild.Parent.NodeKey, 100
        )

    def test_node_successor_parent_is_node_delete_not_leaf(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(120, 4)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 4)
        self.assertTrue(tree.DeleteNodeByKey(75))
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.NodeKey, 50)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(tree.Root.RightChild.NodeKey, 100)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 50)
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey, 60)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 120)
        self.assertEqual(
            tree.Root.RightChild.RightChild.Parent.NodeKey, 100
        )
        self.assertEqual(
            tree.Root.RightChild.LeftChild.RightChild.NodeKey, 65
        )
        self.assertIsNone(
            tree.Root.RightChild.LeftChild.LeftChild
        )
        self.assertEqual(
            tree.Root.RightChild.LeftChild.Parent.NodeKey, 100
        )

    def test_WideAllNodes(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(120, 4)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 4)
        all_nodes = tree.WideAllNodes()
        
        self.assertEqual(tree.Count(), len(all_nodes))

        
    def test_DeepAllNodesInOrder(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(120, 4)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 4)
        all_nodes = tree.DeepAllNodes(0)
               
        self.assertEqual(tree.Count(), len(all_nodes))

        self.assertEqual(all_nodes[0].NodeKey, 25)
        self.assertEqual(all_nodes[1].NodeKey, 50)
        self.assertEqual(all_nodes[2].NodeKey, 60)
        self.assertEqual(all_nodes[3].NodeKey, 65)
        self.assertEqual(all_nodes[4].NodeKey, 75)
        self.assertEqual(all_nodes[5].NodeKey, 100)
        self.assertEqual(all_nodes[6].NodeKey, 120)

    def test_DeepAllNodesPostOrder(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(120, 4)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 4)
        all_nodes = tree.DeepAllNodes(1)
               
        self.assertEqual(tree.Count(), len(all_nodes))
        
        self.assertEqual(all_nodes[0].NodeKey, 25)
        self.assertEqual(all_nodes[1].NodeKey, 65)
        self.assertEqual(all_nodes[2].NodeKey, 60)
        self.assertEqual(all_nodes[3].NodeKey, 120)
        self.assertEqual(all_nodes[4].NodeKey, 100)
        self.assertEqual(all_nodes[5].NodeKey, 75)
        self.assertEqual(all_nodes[6].NodeKey, 50)
        
    def test_DeepAllNodesPostOrder(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(120, 4)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 4)
        all_nodes = tree.DeepAllNodes(2)
               
        self.assertEqual(tree.Count(), len(all_nodes))
        
        self.assertEqual(all_nodes[0].NodeKey, 50)
        self.assertEqual(all_nodes[1].NodeKey, 25)
        self.assertEqual(all_nodes[2].NodeKey, 75)
        self.assertEqual(all_nodes[3].NodeKey, 60)
        self.assertEqual(all_nodes[4].NodeKey, 65)
        self.assertEqual(all_nodes[5].NodeKey, 100)
        self.assertEqual(all_nodes[6].NodeKey, 120)
    
    def test_inversion(self):
        tree = BST(None)
        tree.AddKeyValue(50, 1)
        self.assertEqual(tree.Root.NodeKey, 50)
        tree.AddKeyValue(25, 2)
        tree.AddKeyValue(75, 2)
        tree.AddKeyValue(100, 3)
        tree.AddKeyValue(120, 4)
        tree.AddKeyValue(60, 3)
        tree.AddKeyValue(65, 4)

        self.assertEqual(tree.Root.NodeKey, 50)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 25)

        # inversionTree = tree.Inversion()
        # self.assertEqual(inversionTree.Root.NodeKey, 50)
        # self.assertEqual(inversionTree.Root.RightChild.NodeKey, 25)
        # self.assertEqual(inversionTree.Root.LeftChild.NodeKey, 75)
        
        