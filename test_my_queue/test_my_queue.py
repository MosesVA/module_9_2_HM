import unittest
from MyQueue.QueueClass import Queue


class TestMyQueue(unittest.TestCase):
    my_queue = Queue(3)

    def test01_is_empty(self):
        self.assertEqual(self.my_queue.is_empty(), True)
        self.my_queue.enqueue(1)
        self.assertEqual(self.my_queue.is_empty(), False)

    def test02_is_full(self):
        self.assertEqual(self.my_queue.is_full(), False)
        self.my_queue.enqueue(2)
        self.my_queue.enqueue(3)
        self.assertEqual(self.my_queue.is_full(), True)

