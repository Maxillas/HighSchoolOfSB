class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        output = []
        node = self.head
        while node is not None:
            if node.value == val:
                output.append(node)
            node = node.next
        return output

    def delete(self, val, all=False):
        node = self.head
        prev_node = None

        while node is not None:
            if node.value == val:
                if prev_node is None:
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                    if all is False:
                        if self.head is not None and self.head.next is None:
                            self.tail = self.head
                        node.next = None
                        break
                    else:
                        temp = node.next
                        node.next = None
                        node = temp
                        if self.head is not None and self.head.next is None:
                            self.tail = self.head
                        continue
                else:
                    prev_node.next = node.next
                    if all is False:
                        if node.next is None:
                            self.tail = prev_node
                        node.next = None
                        break
                    elif node.next is not None and node.next.value == val:
                        node = node.next
                        continue
                if node.next is None:
                    self.tail = prev_node
            prev_node = node
            node = node.next

    def clean(self):
        node = self.head
        while node is not None:
            temp = node.next
            node.next = None
            node = temp
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        output = 0
        while node is not None:
            output += 1
            node = node.next
        return output

    def insert(self, afterNode, newNode):
        if afterNode is None:
            node = self.head
            self.head = newNode
            newNode.next = node
            if self.head.next is None:
                self.tail = self.head

        else:
            node = afterNode.next
            afterNode.next = newNode
            newNode.next = node
            if node is None and self.head is not None:
                self.tail = newNode