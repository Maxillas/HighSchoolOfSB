class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.size

    def is_key(self, key):
        index = self.hash_fun(key)
        count = 0

        while self.values[index] != key:
            index += 1
            count += 1
            if index > self.size - 1:
                index = index % self.size
                count += 1
            if count == self.size:
                return False
        return True

    def put(self, key, value):
        index = self.hash_fun(key)
        temp = index
        count = 0
        while self.values[index] is not None:
            if self.values[index] == key:
                self.slots[index] = value
                return
            index += 1
            count += 1
            if index > self.size - 1:
                index = index % self.size
                count += 1
            if count == self.size:
                return
        self.slots[index] = value
        self.values[index] = key

    def get(self, key):
        if self.is_key(key) is False:
            return None
        index = self.hash_fun(key)
        count = 0
        while self.values[index] != key:
            index += 1
            count += 1
            if index > self.size - 1:
                index = index % self.size
                count += 1
            if count == self.size:
                return None
        return self.slots[index]
