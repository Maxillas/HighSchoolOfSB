import unittest
import math

class ksort:

    def __init__(self):
        self.items = [None] * 800
        
    def index(self, s):
        if len(s) != 3 or not (s[0].lower() >= 'a' and s[0].lower() <= 'h') or not s[1:].isdigit():
            return -1
        d0 = 0 
        d1 = 0
        d2 = 0
        for i in range(97, 105, 1):
            if(ord(s[0]) == i):
                d0 = i - 97
                break

        for i in range(48, 58, 1):
            if(ord(s[1]) == i):
                d1 = i - 48
                break

        for i in range(48, 58, 1):
            if(ord(s[2]) == i):
                d2 = i - 48
                break

        return int(d0 * 100 + d1 * 10 + d2)
        
    def add(self, string):
        idx = self.index(string)
        if idx == -1:
            return False
        self.items[idx] = string
        return True     



class TestBST(unittest.TestCase):
    
    def test_index(self):
        s1 = "a01"
        s2 = "b64"
        s3 = "g99"
        k = ksort()
        self.assertEqual(k.index(s1), 1)
        self.assertEqual(k.index(s2), 164)
        self.assertEqual(k.index(s3), 699)
        self.assertEqual(k.index("h99"), 799)

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