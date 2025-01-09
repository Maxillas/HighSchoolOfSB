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

        return int(d0 * 100 + d1 * 10 + d2)
        
    def add(self, string):
        idx = self.index(string)
        if idx == -1:
            return False
        self.items.insert(idx, string)
        return True     
