class TestBS(unittest.TestCase):
    
    def test_Step(self):
        search = BinarySearch([1,2,3,4,5,6,7,8])
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, 7)
        self.assertEqual(search.complete, 0)

        search.Step(2)
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, 2)
        self.assertEqual(search.complete, 0)

        search.Step(2)
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, 2)
        self.assertEqual(search.complete, 1)

    def test_Step2(self):
        search = BinarySearch([10])
        search.Step(15)
        self.assertEqual(search.array, [10])
        self.assertEqual(search.GetResult(), -1)

    def test_Step3(self):
        search = BinarySearch([10, 12, 13, 14, 16])
        search.Step(15)
        self.assertEqual(search.GetResult(), 0)
        search.Step(15)
        self.assertEqual(search.GetResult(), -1)


if __name__ == '__main__':
    unittest.main()
