import Stack
from Stack import Stack

class StringExecutor:
    def stringexecutor(self, string):
        stack = Stack()

        for i in string:
            if i == "(":
                stack.push(i)
            elif stack.pop() == '(':
                continue
            else:
                return False

        return not stack.size()