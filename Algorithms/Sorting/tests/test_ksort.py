class TestBST(unittest.TestCase):
    
    def test_index(self):
        s1 = "a01"
        s2 = "b64"
        s3 = "g99"
        k = ksort()
        self.assertEqual(k.index(s1), 1)
        self.assertEqual(k.index(s2), 164)
        self.assertEqual(k.index(s3), 699)

    def test_add(self):
        s1 = "a01"
        s2 = "b64"
        s3 = "g99"
        s4 = "a02"
        s5 = "a06"
        s6 = "a04"
        k = ksort()
        self.assertEqual(k.add(s1), True)
        
        self.assertEqual(k.items[1], "a01")

        self.assertEqual(k.add(s2), True)
        self.assertEqual(k.items[1], "a01")
        self.assertEqual(k.items[164], "b64")
        
        self.assertEqual(k.add(s3), True)
        self.assertEqual(k.items[1], "a01")
        self.assertEqual(k.items[164], "b64")
        self.assertEqual(k.items[699], "g99")

        self.assertEqual(k.add(s4), True)
        self.assertEqual(k.items[1], "a01")
        self.assertEqual(k.items[2], "a02")
        self.assertEqual(k.items[164], "b64")
        self.assertEqual(k.items[699], "g99")
        self.assertEqual(k.items[2], "a02")

        self.assertEqual(k.add(s5), True)
        self.assertEqual(k.add(s6), True)
    
        self.assertEqual(k.items[1], "a01")
        self.assertEqual(k.items[2], "a02")
        self.assertEqual(k.items[164], "b64")
        self.assertEqual(k.items[699], "g99")
        self.assertEqual(k.items[2], "a02")
        self.assertEqual(k.items[6], "a06")
        self.assertEqual(k.items[4], "a04")


if __name__ == '__main__':
    unittest.main()
