class BinarySearch:

    def __init__(self, array):
        if not array:
            raise ValueError("Массив не может быть пустым.")
        self.Left = 0
        self.Right = len(array) - 1
        self.array = array
        self.complete = 0

    def Step(self, N):
        if(self.complete != 0):
            return
        
        centerIndex = self.Left + (self.Right - self.Left) // 2
        center = self.array[centerIndex]

        if(center == N):
            self.complete = 1
            return
        elif(N < center):
            self.Right = centerIndex - 1
        elif(N > center):
            self.Left = centerIndex + 1

        if(self.Left >= self.Right):
            if 0 <= self.Left < len(self.array) and 0 <= self.Right < len(self.array):
                if(self.array[self.Left] == N or self.array[self.Right] == N):
                    self.complete = 1
                    return
            self.complete = -1
            return
        
    def GetResult(self):
        return self.complete
