import unittest
#import hoare

class TestBST(unittest.TestCase):
    
    def test_ArrayChunk(self):
        test1 = [7,5,6,4,3,1,2]
        self.assertEqual(ArrayChunk(test1), 3)
        self.assertEqual(test1, [2,1,3,4,6,5,7])

        test3 = [1,3,4,6,5,2,8]
        self.assertEqual(ArrayChunk(test3), 5)
        self.assertEqual(test3, [1,3,4,2,5,6,8])

        test2 = [7,5,6,4,3,1]
        self.assertEqual(ArrayChunk(test2), 2)
        self.assertEqual(test2, [1,3,4,6,5,7])

    def test_QuickSort(self):
        test1 = [7,5,6,4,3,1,2]
        QuickSort(test1, 0, len(test1) - 1)
        self.assertEqual(test1, [1,2,3,4,5,6,7])

        test2 = [7,5,6,4,3,1]
        QuickSort(test2, 0, len(test2) - 1)
        self.assertEqual(test2, [1,3,4,5,6,7])

    def test_QuickSortOptimization(self):
        test1 = [7,5,6,4,3,1,2]
        QuickSortTailOptimization(test1, 0, len(test1) - 1)
        self.assertEqual(test1, [1,2,3,4,5,6,7])

        test2 = [7,5,6,4,3,1]
        QuickSortTailOptimization(test2, 0, len(test2) - 1)
        self.assertEqual(test2, [1,3,4,5,6,7])



if __name__ == '__main__':
    unittest.main()
