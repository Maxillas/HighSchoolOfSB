import unittest
from BinarySimpleTreeArray import aBST


class TestaBST(unittest.TestCase):
    
    def test_FindNodeByKey(self):
        bstArray = aBST(3)
        self.assertEqual(len(bstArray.Tree), 15)
        bstArray = aBST(2)
        self.assertEqual(len(bstArray.Tree), 7)
        bstArray = aBST(4)
        self.assertEqual(len(bstArray.Tree), 31)
        bstArray = aBST(0)
        self.assertEqual(len(bstArray.Tree), 1)
        bst = aBST(2)
        self.assertEqual(bst.FindKeyIndex(0), 0)
        self.assertEqual(bst.FindKeyIndex(1), 0)
        self.assertEqual(bst.FindKeyIndex(2), 0)
        self.assertEqual(bst.FindKeyIndex(3), 0)
        
        self.assertEqual(bst.AddKey(10), 0)
        self.assertEqual(bst.Tree[0], 10)
        self.assertEqual(bst.Tree[1], None)
        self.assertEqual(bst.Tree[2], None)
        self.assertEqual(bst.FindKeyIndex(5), -1)
        self.assertEqual(bst.AddKey(5), 1)
        self.assertEqual(bst.FindKeyIndex(15), -2)
        self.assertEqual(bst.AddKey(15), 2)
        self.assertEqual(bst.FindKeyIndex(3), -3)
        self.assertEqual(bst.AddKey(3), 3)
        self.assertEqual(bst.FindKeyIndex(7), -4)
        self.assertEqual(bst.AddKey(7), 4)
        self.assertEqual(bst.FindKeyIndex(17), -6)
        self.assertEqual(bst.AddKey(17), 6)
        self.assertEqual(bst.FindKeyIndex(20), None)
        self.assertEqual(bst.AddKey(20), -1)
        self.assertEqual(bst.AddKey(16), -1)
        self.assertEqual(bst.FindKeyIndex(5), 1)
        self.assertEqual(bst.FindKeyIndex(17), 6)

if __name__ == '__main__':
    unittest.main()