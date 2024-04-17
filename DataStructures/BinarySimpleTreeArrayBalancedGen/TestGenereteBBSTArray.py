import unittest
from GenerateBBSTArray import GenerateBBSTArray


class TestaBST(unittest.TestCase):
    
    def test_FindNodeByKey(self):
        unorderedmas = [3, 4, 7, 6, 1, 2, 5]
        ordered = GenerateBBSTArray(unorderedmas)
        self.assertEqual(ordered[0], 4)
        self.assertEqual(ordered[1], 2)
        self.assertEqual(ordered[2], 6)
        self.assertEqual(ordered[3], 1)
        self.assertEqual(ordered[4], 3)
        self.assertEqual(ordered[5], 5)
        self.assertEqual(ordered[6], 7)

        unorderedmas = [2]
        ordered = GenerateBBSTArray(unorderedmas)
        self.assertEqual(ordered[0], 2)
        self.assertEqual(len(ordered), 1)


if __name__ == '__main__':
    unittest.main()