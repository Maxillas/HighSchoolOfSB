import math

class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.heapSize = 0

    def MakeHeap(self, a, depth):
        arraySize = 0
        while depth >= 0:
            arraySize += 2 ** depth
            depth -= 1
        self.HeapArray = [None] * arraySize
        for i in range(len(a)):
            self.HeapArray[i] = a[i]
            self.heapSize += 1
        for i in range(len(a) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, index):

        while(1):
            leftChildIndex = index * 2 + 1
            rightChildIndex = index * 2 + 2
            largestIndex = index

            if leftChildIndex < self.heapSize and self.HeapArray[leftChildIndex] > self.HeapArray[largestIndex]:
                largestIndex = leftChildIndex
            if rightChildIndex < self.heapSize and self.HeapArray[rightChildIndex] > self.HeapArray[largestIndex]:
                largestIndex = rightChildIndex

            if largestIndex == index:
                return
            temp = self.HeapArray[index]
            self.HeapArray[index] = self.HeapArray[largestIndex]
            self.HeapArray[largestIndex] = temp
            index = largestIndex

    def GetMax(self):
        if self.heapSize == 0:
            return -1
        result = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.heapSize - 1]
        self.HeapArray[self.heapSize - 1] = None
        self.heapSize -= 1
        self.heapify(0)
        return result

    def Add(self, key):
        if len(self.HeapArray) == self.heapSize:
            return False  # если куча вся заполнена
        self.HeapArray[self.heapSize] = key
        self.heapSize += 1
        maxIndex = self.heapSize - 1
        parentIndex = (maxIndex - 1) // 2
        while maxIndex > 0 and (self.HeapArray[parentIndex] < self.HeapArray[maxIndex]):
            temp = self.HeapArray[maxIndex]
            self.HeapArray[maxIndex] = self.HeapArray[parentIndex]
            self.HeapArray[parentIndex] = temp
            maxIndex = parentIndex
            parentIndex = (maxIndex - 1) // 2


class HeapSort:
    
    def __init__(self, array):
        self.HeapObject = Heap()
        if(len(array) == 0):
            return
        deep = int(math.log2(len(array)))
        self.HeapObject.MakeHeap(array, deep)
        
    def GetNextMax(self):
        if(self.HeapObject.heapSize == 0):
            return -1
        return self.HeapObject.GetMax()
