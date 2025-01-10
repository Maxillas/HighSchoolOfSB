class BinarySearch:

    def __init__(self, array):
        if not array:
            raise ValueError("Массив не может быть пустым.")
        self.left = 0
        self.right = len(array) - 1
        self.array = array
        self.complete = 0

    def Step(self, N):
        if(self.complete != 0):
            return
        
        centerIndex = self.left + (self.right - self.left) // 2
        center = self.array[centerIndex]

        if(center == N):
            self.complete = 1
            return
        elif(N < center):
            self.right = centerIndex - 1
        elif(N > center):
            self.left = centerIndex + 1

        if(self.left >= self.right):
            if 0 <= self.left < len(self.array) and 0 <= self.right < len(self.array):
                if(self.array[self.left] == N or self.array[self.right] == N):
                    self.complete = 1
                    return
            self.complete = -1
            return
        
    def GetResult(self):
        return self.complete
