class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:

    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value):
        input_node = Node(value)
        node = self.head

        def add_in_head(self, node, input_node):
            self.head = input_node
            input_node.next = node
            node.prev = input_node

        def add_in_tail(self, node, input_node):
            self.tail = input_node
            node.next = input_node
            input_node.prev = node

        def add_in_middle(self, node, input_node):
            temp = node.next
            node.next = input_node
            input_node.prev = node
            input_node.next = temp
            temp.prev = input_node

        if node is None:
            self.head = input_node
            self.tail = input_node
            return

        while node is not None:
            compare = self.compare(input_node.value, node.value)

            if node.next is None and (compare >= 0) and self.__ascending is True:
                add_in_tail(self, node, input_node)
                return
            elif (node.next is None or node.prev is None) and compare >= 0 and self.__ascending is False:
                add_in_head(self, node, input_node)
                return
            elif (node.next is None or node.prev is None) and compare <= 0 and self.__ascending is True:
                add_in_head(self, node, input_node)
                return
            elif node.next is None and compare <= 0 and self.__ascending is False:
                add_in_tail(self, node, input_node)
                return

            compare_next = self.compare(input_node.value, node.next.value)

            if compare >= 0 and compare_next <= 0 and self.__ascending is True:
                add_in_middle(self, node, input_node)
                return
            elif compare <= 0 and compare_next >= 0 and self.__ascending is False:
                add_in_middle(self, node, input_node)
                return

            node = node.next

    def find(self, val):
        node = self.head
        if val < node.value and self.__ascending is True:
            return None
        if val > node.value and self.__ascending is False:
            return None

        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
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

    def clean(self, asc):
        self.__ascending = asc
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

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        str1 = v1.strip()
        str2 = v2.strip()

        if str1 < str2:
            return -1
        if str1 > str2:
            return 1
        return 0