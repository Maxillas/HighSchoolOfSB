class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_list = 0

    def hash1(self, str1):
        rand_const = 17
        index = 0
        for c in str1:
            code = ord(c)
            index = (index * rand_const + code) % self.filter_len
        return 1 << index

    def hash2(self, str1):
        rand_const = 223
        index = 0
        for c in str1:
            code = ord(c)
            index = (index * rand_const + code) % self.filter_len
        return 1 << index

    def add(self, str1):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        self.bit_list = self.bit_list | (index1 | index2)

    def is_value(self, str1):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        return self.bit_list & index1 != 0 and self.bit_list & index2 != 0
