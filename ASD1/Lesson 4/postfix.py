import Stack
from Stack import Stack


class Postfix:

    def postfix(self, stack1):
        stack2 = Stack()
        while stack1.size() != 0:
            temp = stack1.pop()
            if type(temp) is int or type(temp) is float:
                stack2.push(temp)
            elif temp != "=":
                second = stack2.pop()
                first = stack2.pop()
                if temp == "+":
                    output = first + second
                elif temp == "-":
                    output = first - second
                elif temp == "*":
                    output = first * second
                elif temp == "/":
                    output = first / second
                stack2.push(output)
            else:
                return stack2.pop()