class PowerSet():

    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def put(self, value):
        if self.get(value) is False:
            self.list.append(value)

    def get(self, value):
        for i in self.list:
            if i == value:
                return True
        return False

    def remove(self, value):
        if self.get(value) is False:
            return False
        self.list.remove(value)
        return True

    def intersection(self, set2):
        output = PowerSet()
        for i in self.list:
            if set2.get(i) is True:
                output.put(i)
        return output

    def union(self, set2):
        output = PowerSet()
        if set2.size == 0:
            return self
        for i in self.list:
            output.put(i)
        for i in set2.list:
            output.put(i)
        return output

    def difference(self, set2):
        output = PowerSet()
        for i in self.list:
            output.put(i)
        for i in set2.list:
            if self.get(i) is True:
                output.remove(i)
        return output

    def issubset(self, set2):
        temp = self
        for i in set2.list:
            if temp.get(i) is False:
                return False
        return True

