import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        temp = None
        flag = False
        if self.count == 0:
            self.append(itm)
            return
        self.append(0)
        for j in range(i, self.count):

            if i == j:
                temp = self.array[j]
                self.array[j] = itm
                flag = True
            elif flag is True and i != self.count - 1:
                temp2 = self.array[j]
                self.array[j] = temp
                temp = temp2

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        flag = False
        for j in range(i, self.count):

            if i == j and j != self.count - 1:
                self.array[j] = self.array[j + 1]
                flag = True
            elif flag is True and j != self.count - 1:
                self.array[j] = self.array[j + 1]

        self.count -= 1

        if self.count < int(self.capacity * 0.5):
            self.capacity = int(self.capacity / 1.5)
        if self.capacity < 16:
            self.capacity = 16

class Deque:
    def __init__(self):
        self.list = DynArray()

    def addFront(self, item):
        self.list.insert(0, item)

    def addTail(self, item):
        self.list.append(item)

    def removeFront(self):
        if self.list.count == 0:
            return None
        temp = self.list[0]
        self.list.delete(0)
        return temp

    def removeTail(self):
        if self.list.count == 0:
            return None
        index_of_last_element = self.list.count - 1
        temp = self.list[index_of_last_element]
        self.list.delete(index_of_last_element)
        return temp

    def size(self):
        return self.list.count