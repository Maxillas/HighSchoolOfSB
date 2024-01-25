from Deque import Deque

class Palindrome():
    def check_palindrome(self, string):
        deque = Deque()
        temp = Deque()
        for i in string:
            deque.addFront(i)
            temp.addFront(i)

        while deque.size() > 0:
            front = deque.removeFront()
            tail = temp.removeTail()
            if front != tail:
                return False
        return True
