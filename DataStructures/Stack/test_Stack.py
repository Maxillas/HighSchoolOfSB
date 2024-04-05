import unittest
import Stack
import StringExecutor
from StringExecutor import StringExecutor
import postfix
from postfix import Postfix

from Stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        stack1 = Stack()
        stack1.push(5)
        stack1.push(15.2)
        stack1.push("hey")
        stack1.push(9)
        stack1.push(23.2)
        stack1.push("uga")

        self.assertEqual(stack1.stack[stack1.stack.count - 1], 5)
        self.assertEqual(stack1.stack[stack1.stack.count - 2], 15.2)
        self.assertEqual(stack1.stack[stack1.stack.count - 3], "hey")
        self.assertEqual(stack1.stack[stack1.stack.count - 4], 9)
        self.assertEqual(stack1.stack[stack1.stack.count - 5], 23.2)
        self.assertEqual(stack1.stack[stack1.stack.count - 6], "uga")

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(5)
        stack.push(15.2)
        stack.push("hey")
        self.assertEqual(stack.size(), 3)
        stack.push(9)
        self.assertEqual(stack.size(), 4)
        stack.push(23.2)
        self.assertEqual(stack.size(), 5)
        stack.push("uga")
        self.assertEqual(stack.size(), 6)

    def test_pop(self):
        stack_first = Stack()
        stack_first.push(5)
        stack_first.push(15.2)
        stack_first.push("hey")
        stack_first.push(9)
        stack_first.push(23.2)
        stack_first.push("uga")

        self.assertEqual(stack_first.size(), 6)
        self.assertEqual(stack_first.pop(), "uga")
        self.assertEqual(stack_first.size(), 5)
        self.assertEqual(stack_first.pop(), 23.2)
        self.assertEqual(stack_first.size(), 4)
        self.assertEqual(stack_first.pop(), 9)
        stack_first.pop()
        stack_first.pop()
        self.assertEqual(stack_first.pop(), 5)
        self.assertEqual(stack_first.pop(), None)

    def test_peek(self):
        stack_first = Stack()
        stack_first.push(5)
        stack_first.push(15.2)
        stack_first.push("hey")
        stack_first.push(9)
        stack_first.push(23.2)
        stack_first.push("uga")

        self.assertEqual(stack_first.size(), 6)
        self.assertEqual(stack_first.peek(), "uga")
        self.assertEqual(stack_first.size(), 6)
        self.assertEqual(stack_first.peek(), "uga")
        stack_first.pop()
        stack_first.pop()
        stack_first.pop()
        stack_first.pop()
        stack_first.pop()
        stack_first.pop()
        self.assertEqual(stack_first.peek(), None)

    def test_stringexecutor(self):

        stringEx = StringExecutor()
        string = "())("
        string1 = "))(("
        string2 = "((())"
        string3 = "(()((())()))"
        string4 = "(()()(()"
        string5 = "(((())))"

        self.assertEqual(stringEx.stringexecutor(string), False)
        self.assertEqual(stringEx.stringexecutor(string1), False)
        self.assertEqual(stringEx.stringexecutor(string2), False)
        self.assertEqual(stringEx.stringexecutor(string3), True)
        self.assertEqual(stringEx.stringexecutor(string4), False)
        self.assertEqual(stringEx.stringexecutor(string5), True)

    def test_postfix(self):
        stack = Stack()
        result = Postfix()

        stack.push("=")
        stack.push("+")
        stack.push(9)
        stack.push("*")
        stack.push(5)
        stack.push("+")
        stack.push(2)
        stack.push(8)

        self.assertEqual(result.postfix(stack), 59)

        stack2 = Stack()
        result = Postfix()

        stack2.push("=")
        stack2.push("-")
        stack2.push(9)
        stack2.push("*")
        stack2.push(5)
        stack2.push("/")
        stack2.push(2)
        stack2.push(8)

        self.assertEqual(result.postfix(stack2), 11)

        stack3 = Stack()
        result = Postfix()

        stack3.push("=")
        stack3.push("-")
        stack3.push(900)
        stack3.push("*")
        stack3.push(50)
        stack3.push("/")
        stack3.push(2)
        stack3.push(800)

        self.assertEqual(result.postfix(stack3), 19100)

        stack4 = Stack()
        result = Postfix()

        stack4.push("=")
        stack4.push("-")
        stack4.push(35.6)
        stack4.push("*")
        stack4.push(2.3)
        stack4.push("/")
        stack4.push(2)
        stack4.push(12.2)

        self.assertEqual(result.postfix(stack4), -21.570000000000004)



