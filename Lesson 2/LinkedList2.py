class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        while node is not None:
            if node.value == val and node == self.head:
                self.head = node.next
                if self.head is not None:
                    self.head.prev = node.prev
                if self.tail == node:
                    self.tail = self.head
                node.next = None
                node.prev = None
                return
            if node.value == val and node == self.tail:
                self.tail = node.prev
                if self.tail is not None:
                    self.tail.next = None
                if node.prev == self.head:
                    self.head = self.tail
                node.prev = None
                node.next = None
                return
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None
                return
            node = node.next

    def clean(self):
        node = self.head
        while node is not None:
            temp = node.next
            node.next = None
            node.prev = None
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
            if self.len() == 0:
                self.add_in_tail(newNode)
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                newNode.next = None
                self.tail = newNode

        else:
            node = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode
            newNode.next = node

            if node is None and self.head is not None:
                self.tail = newNode
            else:
                node.prev = newNode


    def add_in_head(self, newNode):

        if self.head is not None:
            temp = self.head
            temp.prev = newNode
            self.head = newNode
            newNode.next = temp
            newNode.prev = None
        else:
            self.head = newNode
            self.tail = newNode
        if self.len() <= 1:
            self.tail = newNode