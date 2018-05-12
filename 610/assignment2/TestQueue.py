import unittest
from QueueADT import *

class TestQueue(unittest.TestCase):
    def test_init(self):
        q = QueueADT(10)
    
    def test_is_full_and_is_empty(self):
        q = QueueADT(3)
        self.assertEqual(False, q.is_full())
        self.assertEqual(True, q.is_empty())
        
        q.enqueue(1)
        self.assertEqual(False, q.is_full())
        self.assertEqual(False, q.is_empty())
        q.enqueue(2)
        self.assertEqual(False, q.is_full())
        self.assertEqual(False, q.is_empty())
        q.enqueue(3)
        self.assertEqual(True, q.is_full())
        self.assertEqual(False, q.is_empty())


    def test_enqueue(self):
        q = QueueADT(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

    def test_dequeue(self):
        q = QueueADT(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(1, q.dequeue())
        self.assertEqual(2, q.dequeue())
        self.assertEqual(3, q.dequeue())


    def test_size(self):
        q = QueueADT(3)
        self.assertEqual(0, q.size())
        q.enqueue(1)
        self.assertEqual(1, q.size())
        q.enqueue(2)
        self.assertEqual(2, q.size())
        q.enqueue(3)
        self.assertEqual(3, q.size())
        q.dequeue()
        self.assertEqual(2, q.size())
        q.dequeue()
        self.assertEqual(1, q.size())
        q.dequeue()
        self.assertEqual(0, q.size())
        

if __name__ == "__main__":
    unittest.main()