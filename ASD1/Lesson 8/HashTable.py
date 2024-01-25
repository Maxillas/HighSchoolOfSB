class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        sum = 0
        for i in value:
            sum += ord(i)
        return sum % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        count = 0
        while self.slots[index] is not None:
            index += self.step
            if index > self.size - 1:
                index = index % self.size
                count += 1
                continue
            if count == 5:
                return None
        return index

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value):
        index = self.hash_fun(value)
        count = 0
        while self.slots[index] != value:
            index += self.step
            if index > self.size - 1:
                index = index % self.size
                count += 1
                continue
            if count == 5:
                return None
        return index
