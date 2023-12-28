import unittest
import Queue
import Rotate
from Queue import Queue
from Rotate import Rotate
from QueueTwoStacks import QueueTwoStacks


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue1 = Queue()
        self.assertEqual(queue1.size(), 0)
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)
        queue1.enqueue(5)


        self.assertEqual(queue1.queue.head.value, 1)
        self.assertEqual(queue1.queue.tail.value, 5)
        self.assertEqual(queue1.size(), 5)
        self.assertEqual(queue1.dequeue(), 1)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.dequeue(), 4)
        self.assertEqual(queue1.dequeue(), 5)
        self.assertEqual(queue1.dequeue(), None)
        self.assertEqual(queue1.size(), 0)
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)
        queue1.enqueue(5)

        self.assertEqual(queue1.queue.head.value, 1)
        self.assertEqual(queue1.queue.tail.value, 5)
        self.assertEqual(queue1.size(), 5)

    def test_rotate(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)
        queue1.enqueue(5)

        rotate = Rotate()
        rotate.rotate(queue1, 3)

        self.assertEqual(queue1.queue.head.value, 4)
        rotate.rotate(queue1, 1)
        self.assertEqual(queue1.queue.head.value, 5)
        rotate.rotate(queue1, 0)
        self.assertEqual(queue1.queue.head.value, 5)

        queue2 = Queue()
        rotate.rotate(queue2, 2)
        self.assertEqual(queue2.queue.head, None)

    def test_QueueTwoStacks(self):
        queue1 = QueueTwoStacks()
        self.assertEqual(queue1.size(), 0)
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)
        queue1.enqueue(5)


        self.assertEqual(queue1.queue.stack[0], 5)
        self.assertEqual(queue1.queue.stack[1], 4)
        self.assertEqual(queue1.size(), 5)
        self.assertEqual(queue1.dequeue(), 1)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.dequeue(), 4)
        self.assertEqual(queue1.dequeue(), 5)
        self.assertEqual(queue1.dequeue(), None)
        self.assertEqual(queue1.size(), 0)
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)
        queue1.enqueue(5)

        self.assertEqual(queue1.queue.stack[0], 5)
        self.assertEqual(queue1.queue.stack[1], 4)
        self.assertEqual(queue1.size(), 5)