import unittest
import math

class ksort:

    def __init__(self):
        self.items = [None] * 700
        
    def index(self, s):
        if len(s) != 3 or not (s[0].lower() >= 'a' and s[0].lower() <= 'h') or not s[1:].isdigit():
            return -1
        d0 = 0 
        d1 = 0
        d2 = 0
        for i in range(97, 104, 1): #ord(s[0])
            if(ord(s[0]) == i):
                d0 = i - 97
                break

        for i in range(48, 57, 1): #ord(s[0])
            if(ord(s[1]) == i):
                d1 = i - 48
                break

        for i in range(48, 57, 1): #ord(s[0])
            if(ord(s[2]) == i):
                d2 = i - 48
                break
            
        print(s, d0, d1, d2)

        return int(d0 * 100 + d1 * 10 + d2)
        #return ord(s[0]) - ord('a')
        
    def add(self, string):
        idx = self.index(string)
        if idx == -1:
            return False
        # for i in range(len(self.items)):
        #     if self.items[i] is None or (idx < 0 and i > idx) or (idx >= 0 and i <= idx):
        #         break
        self.items.insert(idx, string)
        return True     


class TestBST(unittest.TestCase):
    
    def test_index(self):
        s1 = "a01"
        s2 = "b64"
        s3 = "g99"
        k = ksort()
        # self.assertEqual(k.index(s1), 699)
        # self.assertEqual(k.index(s2), 699)
        # self.assertEqual(k.index(s3), 699)
        # self.assertEqual(k.index("132"), -1)
        # self.assertEqual(k.index("n32"), -1)
        # self.assertEqual(k.index("ag32"), -1)
        # self.assertEqual(k.index("a321"), -1)

    def test_add(self):
        s1 = "a01"
        s2 = "b64"
        s3 = "g99"
        s4 = "a02"
        s5 = "a06"
        s6 = "a04"
        k = ksort()
        self.assertEqual(k.add(s1), True)
        #print(k.items)
        #self.assertEqual(k.items[699], "a01")

        self.assertEqual(k.add(s2), True)
        #print(k.items)
        #self.assertEqual(k.items[699], "a01")
        #self.assertEqual(k.items[698], "b64")
        
        self.assertEqual(k.add(s3), True)
        self.assertEqual(k.add(s4), True)
        self.assertEqual(k.add(s5), True)
        self.assertEqual(k.add(s6), True)
        print(k.items)

    
        #self.assertEqual(k.items[699], "a01")
        #self.assertEqual(k.items[698], "b64")
        #self.assertEqual(k.items[697], "g99")


if __name__ == '__main__':
    unittest.main()
