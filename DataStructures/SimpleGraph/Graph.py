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
        else:
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


class Stack:
    def __init__(self):
        self.stack = DynArray()

    def size(self):
        return self.stack.count

    def pop(self):
        if self.stack.count == 0:
            temp = None
        else:
            temp = self.stack[0]
            self.stack.delete(0)
        return temp

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.stack.count == 0:
            temp = None
        else:
            temp = self.stack[0]
        return temp
    
class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.stack = Stack()

    def AddVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return
        return
        # здесь и далее, параметры v -- индекс вершины
        # в списке  vertex

    def RemoveVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                continue
            if self.vertex[i].Value == v:
                self.vertex[i] = None
                for i in range(self.max_vertex - 1):
                    self.m_adjacency[1][i] = 0
                    self.m_adjacency[i][1] = 0
        # ваш код удаления вершины со всеми её рёбрами

    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1:
            return True
        return False
        # True если есть ребро между вершинами v1 и v2

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2
        
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        # удаление ребра между вершинами v1 и v2
        pass

    def clearStack(self):
        i = self.stack.pop()
        while i != None:
            i = self.stack.pop()
            continue    

    def clearHit(self):
        for i in self.vertex:
            i.hit = False

    def searchTargetInSelf(self, startIndex, endIndex):
        for i in range(len(self.m_adjacency[startIndex])):
            if self.vertex[i].hit is True:
                currentVertex = self.vertex[i]
                return self.search(currentVertex, startIndex, endIndex)
        return

    def search(self, currentVertex, startIndex, endIndex):
        currentVertex.hit = True
        self.stack.push(currentVertex)

        for i in range(len(self.m_adjacency[startIndex])):
            if self.m_adjacency[startIndex][i] == 1:
                self.stack.push(self.vertex[i])
                return self.stack
        if self.searchTargetInSelf(startIndex, endIndex) is None:
            #реализовать это в главной функции, где вызывать эти функции частично
        upperElement = self.stack.pop()
        if self.stack.size == 0:
            return # path not found
        else:
            currentVertex = upperElement
            currentVertex.hit = True





    def DepthFirstSearch(self, startIndex, endIndex):
        
        self.clearStack()
        self.clearHit()
        currentVertex = self.vertex[startIndex]

        search(currentVertex, startIndex, endIndex)
        
        
        # удаление ребра между вершинами v1 и v2
        pass
