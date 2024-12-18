import unittest

class TestMergeSort(unittest.TestCase):
    
    def test_Divide(self):
        test1 = [1,5,7,4,2,3,6]
        result = MergeSort(test1)
        self.assertEqual(result, [1,2,3,4,5,6,7])

        test2 = [1,5,7,4,2,3]
        result = MergeSort(test2)
        self.assertEqual(result, [1,2,3,4,5,7])
        

if __name__ == '__main__':
    unittest.main()
