import unittest
import HeapSort

class TestBST(unittest.TestCase):
    
    def test_Heap(self):
        array = [3,1,2,5,4]
        heap = HeapSort(array)
        self.assertEqual(heap.GetNextMax(), 5)
        self.assertEqual(heap.GetNextMax(), 4)
        self.assertEqual(heap.GetNextMax(), 3)
        self.assertEqual(heap.GetNextMax(), 2)
        self.assertEqual(heap.GetNextMax(), 1)
        self.assertEqual(heap.GetNextMax(), -1)

        array = []
        heap = HeapSort(array)
        self.assertEqual(heap.GetNextMax(), -1)


if __name__ == '__main__':
    unittest.main()
