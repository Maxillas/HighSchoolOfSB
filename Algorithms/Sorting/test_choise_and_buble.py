import unittest
import choise_and_buble

class TestBST(unittest.TestCase):
    
    def test_SelectionSort(self):
        test1 = [4,3,1,2]

        SelectionSortStep(test1, 0)
        self.assertEqual(test1, [1,3,4,2])
        SelectionSortStep(test1, 1)
        self.assertEqual(test1, [1,2,4,3])
        SelectionSortStep(test1, 2)
        self.assertEqual(test1, [1,2,3,4])
        SelectionSortStep(test1, 3)
        self.assertEqual(test1, [1,2,3,4])

        test2 = []

        SelectionSortStep(test2, 0)
        self.assertEqual(test2, [])
        SelectionSortStep(test2, 1)
        self.assertEqual(test2, [])

    def test_BubbleSortStep(self):
        test1 = [4,3,1,2]    
        
        BubbleSortStep(test1)
        self.assertEqual(test1, [3,1,2,4])
        BubbleSortStep(test1)
        self.assertEqual(test1, [1,2,3,4])
        BubbleSortStep(test1)
        self.assertEqual(test1, [1,2,3,4])

if __name__ == '__main__':
    unittest.main()