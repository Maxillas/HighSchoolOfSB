class TestBS(unittest.TestCase):
    
    def test_step(self):
        search = BinarySearch([1,2,3,4,5,6,7,8])
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.left, 0)
        self.assertEqual(search.right, 7)
        self.assertEqual(search.complete, 0)

        search.Step(2)
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.left, 0)
        self.assertEqual(search.right, 2)
        self.assertEqual(search.complete, 0)

        search.Step(2)
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.left, 0)
        self.assertEqual(search.right, 2)
        self.assertEqual(search.complete, 1)


if __name__ == '__main__':
    unittest.main()
