class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 0
        while depth >= 0:
            tree_size += 2 ** depth
            depth -= 1
        self.Tree = [None] * tree_size # массив ключей
  
    def FindKeyIndex(self, key):
                
        def find(key, index):
            if index >= len(self.Tree):
                return None
            if self.Tree[index] == None:
                return -index
            if key == self.Tree[index]:
                return index
            if key > self.Tree[index]:
                index = (2 * index) + 2
                return find(key, index)
            if key < self.Tree[index]:
                index = (2 * index) + 1
                return find(key, index)
        return find(key, 0)
    
    def AddKey(self, key):
        
        index = self.FindKeyIndex(key)
        if index == None:
            return -1
        if index <= 0:
            self.Tree[-index] = key
            return -index
        return index

