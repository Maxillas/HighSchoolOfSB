import unittest
import insert

def InsertionSortStep(array, step, i):
        
    for index in range (i + step, len(array), step):
        for inserIndex in range (i, index, step):
            if(array[index] < array[inserIndex]):
                array[index], array[inserIndex] = array[inserIndex], array[index]




class TestBST(unittest.TestCase):
    
    def test_InsertSort(self):
        test1 = [7,6,5,4,3,2,1]

        InsertionSortStep(test1, 3, 0)
        self.assertEqual(test1, [1,6,5,4,3,2,7])
        InsertionSortStep(test1, 3, 1)
        self.assertEqual(test1, [1,3,5,4,6,2,7])
        InsertionSortStep(test1, 3, 2)
        self.assertEqual(test1, [1,3,2,4,6,5,7])
        InsertionSortStep(test1, 3, 3)
        self.assertEqual(test1, [1,3,2,4,6,5,7])

        test2 = []

        InsertionSortStep(test1, 3, 0)
        self.assertEqual(test2, [])
        InsertionSortStep(test1, 3, 0)
        self.assertEqual(test2, [])


if __name__ == '__main__':
    unittest.main()