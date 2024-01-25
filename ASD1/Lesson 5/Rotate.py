import Queue
from Queue import Queue

class Rotate:

    def rotate(self, queue, N):
        if queue.size() == 0:
            return
        for i in range(N):
            temp = queue.dequeue()
            queue.enqueue(temp)


