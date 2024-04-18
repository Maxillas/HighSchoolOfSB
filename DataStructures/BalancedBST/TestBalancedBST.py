import unittest
from BalancedBST import BalancedBST

class TestBST(unittest.TestCase):
    
    def test_Generator(self):
        list = [2, 5, 1, 4, 3, 7, 6] 
        #[1, 2, 3, 4, 5, 6, 7]
        tree = BalancedBST()

        tree.GenerateTree(list)

        self.assertEqual(tree.Root.NodeKey, 4)
        self.assertEqual(tree.Root.Level, 0)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 2)
        self.assertEqual(tree.Root.RightChild.NodeKey, 6)
        self.assertEqual(tree.Root.LeftChild.Level, 1)
        self.assertEqual(tree.Root.RightChild.Level, 1)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 4)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 4)
        self.assertEqual(tree.Root.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(tree.Root.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(tree.Root.LeftChild.LeftChild.Level, 2)
        self.assertEqual(tree.Root.LeftChild.RightChild.Level, 2)
        self.assertEqual(tree.Root.LeftChild.LeftChild.Parent.NodeKey, 2)
        self.assertEqual(tree.Root.LeftChild.RightChild.Parent.NodeKey, 2)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 7)
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 4)
        self.assertEqual(tree.Root.RightChild.RightChild.Parent.NodeKey, 6)
        self.assertEqual(tree.Root.RightChild.LeftChild.Parent.NodeKey, 6)

        
        self.assertEqual(tree.IsBalanced(tree.Root), True)
        self.assertEqual(tree.IsBalanced(tree.Root.LeftChild), True)
        self.assertEqual(tree.IsBalanced(tree.Root.RightChild), True)
        self.assertEqual(tree.IsBalanced(tree.Root.RightChild.RightChild), True)
        tree.Root.RightChild = None
        self.assertEqual(tree.IsBalanced(tree.Root), False)    

if __name__ == '__main__':
    unittest.main()