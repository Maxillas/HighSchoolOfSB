import unittest
from Heap import Heap


class TestBST(unittest.TestCase):
    
    def test_FindNodeByKey(self):
        heap = Heap()
        heap.MakeHeap([5, 1, 3, 7, 4], 2)
        self.assertEqual(heap.HeapArray[0], 7)
        self.assertEqual(heap.heapSize, 5)
        self.assertEqual(len(heap.HeapArray), 7)
        heap.Add(2)
        self.assertEqual(heap.HeapArray[0], 7)
        self.assertEqual(heap.heapSize, 6)
        self.assertEqual(len(heap.HeapArray), 7)
        heap.Add(10)
        self.assertEqual(heap.HeapArray[0], 10)
        self.assertEqual(heap.heapSize, 7)
        self.assertEqual(len(heap.HeapArray), 7)

        self.assertEqual(heap.Add(16), False)
        self.assertEqual(heap.HeapArray[0], 10)
        self.assertEqual(heap.heapSize, 7)
        self.assertEqual(len(heap.HeapArray), 7)

    def test_FindNodeByKey(self):
        heap = Heap()
        heap.MakeHeap([5, 1, 3, 7, 4], 2)
        heap.Add(2)
        heap.Add(10)

        self.assertEqual(heap.GetMax(), 10)
        self.assertEqual(heap.HeapArray[0], 7)
        self.assertEqual(heap.heapSize, 6)
        self.assertEqual(len(heap.HeapArray), 7)
        self.assertEqual(heap.GetMax(), 7)
        self.assertEqual(heap.GetMax(), 5)
        self.assertEqual(heap.GetMax(), 4)
        self.assertEqual(heap.GetMax(), 3)
        self.assertEqual(heap.GetMax(), 2)
        self.assertEqual(heap.GetMax(), 1)
        self.assertEqual(heap.GetMax(), -1)

if __name__ == '__main__':
    unittest.main()