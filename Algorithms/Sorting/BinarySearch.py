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
        
        centerIndex = (self.Right + self.Left) // 2 #self.Left + (self.Right - self.Left) // 2
        center = self.array[centerIndex]

        if(center == N):
            self.complete = 1
            return
        elif(N < center):
            self.Right = centerIndex - 1
        else:
            self.Left = centerIndex + 1

        if self.Left > self.Right:
            self.complete = -1
            return
        elif self.Left == self.Right or abs(self.Left - self.Right) == 1:
            if self.array[self.Left] == N or self.array[self.Right] == N:
                self.complete = 1
            else:
                self.complete = -1
            return
                
    def GetResult(self):
        return self.complete

def GallopingSearch(array, N):

    if not array:
        raise ValueError("Массив не может быть пустым.")

    if len(array) == 1:
        return array[0] == N

    i = 1
    index = 0
    while ((index < (len(array) - 1)) and array[index] < N):
        if(array[index] == N):
            return True
        index = 2 ** i - 2
        i += 1
    i -= 1
    if(index >= (len(array))):
        index = len(array) - 1

    if(array[index] == N):
        return True

    if array[index] > N:
        bs = BinarySearch(array)
        bs.Left = max((2 ** (i - 1) - 2) + 1, 0)  # Левая граница
        bs.Right = min(index, len(array) - 1)     # Правая граница

        while bs.complete == 0:
            bs.Step(N)

        return bs.complete == 1

    return False
