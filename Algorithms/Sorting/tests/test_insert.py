import unittest
import insert

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
    def test_ShellSort(self):
        test1 = [7,6,5,4,3,2,1]

        
        self.assertEqual(SequenceElem(1), 4)
        self.assertEqual(SequenceElem(2), 13)
        self.assertEqual(SequenceElem(3), 40)
        self.assertEqual(SequenceElem(4), 121)
        self.assertEqual(SequenceElem(5), 364)

        self.assertEqual(KnuthSequence(15), [13,4,1])
        self.assertEqual(KnuthSequence(13), [13,4,1])
        self.assertEqual(KnuthSequence(12), [4,1])
        self.assertEqual(KnuthSequence(4), [4,1])
        self.assertEqual(KnuthSequence(3), [4,1])
        self.assertEqual(KnuthSequence(350), [364,13,4,1])
        self.assertEqual(KnuthSequence(367), [364,4,1])
        self.assertEqual(KnuthSequence(0), [])
        self.assertEqual(KnuthSequence(1), [1])
                
        test5 = [5,6,7,1,4,2,3]
        ShellSorting(test5)
        self.assertEqual(test5, [1,2,3,4,5,6,7])

if __name__ == '__main__':
    unittest.main()
