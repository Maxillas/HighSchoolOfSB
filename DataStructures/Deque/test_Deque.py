import unittest

from Deque import Deque
from Palindrome import Palindrome


class TestDeqeu(unittest.TestCase):

    def test_add(self):
        deque1 = Deque()
        self.assertEqual(deque1.size(), 0)
        deque1.addFront(1)
        deque1.addFront(2)
        deque1.addFront(3)
        deque1.addFront(4)
        deque1.addFront(5)
        self.assertEqual(deque1.size(), 5)

        deque1.addTail(1)
        deque1.addTail(2)
        deque1.addTail(3)
        deque1.addTail(4)
        deque1.addTail(5)
        self.assertEqual(deque1.size(), 10)

    def test_remove(self):
        deque1 = Deque()
        deque1.addFront(1)
        self.assertEqual(deque1.list[0], 1)
        deque1.addFront(2)
        self.assertEqual(deque1.list[0], 2)
        deque1.addFront(3)
        deque1.addFront(4)
        deque1.addFront(5)
        self.assertEqual(deque1.removeFront(), 5)
        self.assertEqual(deque1.size(), 4)
        self.assertEqual(deque1.removeTail(), 1)
        self.assertEqual(deque1.size(), 3)

        deque1.addTail(10)
        self.assertEqual(deque1.list[0], 4)
        self.assertEqual(deque1.list[deque1.list.count - 1], 10)
        deque1.addTail(20)
        deque1.addTail(30)
        deque1.addTail(40)
        deque1.addTail(50)
        self.assertEqual(deque1.removeFront(), 4)
        self.assertEqual(deque1.removeTail(), 50)
        self.assertEqual(deque1.removeFront(), 3)
        self.assertEqual(deque1.removeFront(), 2)
        self.assertEqual(deque1.removeFront(), 10)
        self.assertEqual(deque1.removeTail(), 40)
        self.assertEqual(deque1.removeTail(), 30)
        self.assertEqual(deque1.removeTail(), 20)
        self.assertEqual(deque1.removeTail(), None)
        self.assertEqual(deque1.removeFront(), None)

        deque1.addTail(10)
        self.assertEqual(deque1.removeFront(), 10)
        deque1.addFront(20)
        self.assertEqual(deque1.removeTail(), 20)

    def testPalindrome(self):
        pal = Palindrome()
        string1 = "adda"
        string2 = "abcd"
        string3 = "aaaa"
        string4 = "aaa"
        string5 = "a"
        string6 = "sos"
        string7 = "aaaaaaaaaa"
        string8 = "aaaaaaaaab"
        self.assertEqual(pal.check_palindrome(string1), True)
        self.assertEqual(pal.check_palindrome(string2), False)
        self.assertEqual(pal.check_palindrome(string3), True)
        self.assertEqual(pal.check_palindrome(string4), True)
        self.assertEqual(pal.check_palindrome(string5), True)
        self.assertEqual(pal.check_palindrome(string6), True)
        self.assertEqual(pal.check_palindrome(string7), True)
        self.assertEqual(pal.check_palindrome(string8), False)

