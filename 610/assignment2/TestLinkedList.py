import unittest
from LinkedListADT import *

class TestLinkedList(unittest.TestCase):
    def test_init(self):
        l = LinkedListADT()
        self.assertEqual(None, l.head)
        self.assertEqual(None, l.tail)

    def test_add_head(self):
        l = LinkedListADT()
        self.assertEqual(None, l.head)
        self.assertEqual(None, l.tail)
        l.add_head(1)
        self.assertEqual(1, l.head.data)
        self.assertEqual(1, l.tail.data)
        l.add_head(2)
        self.assertEqual(2, l.head.data)
        self.assertEqual(1, l.tail.data)
        
    def test_add_tail(self):
        l = LinkedListADT()
        self.assertEqual(None, l.head)
        self.assertEqual(None, l.tail)
        l.add_tail(1)
        self.assertEqual(1, l.head.data)
        self.assertEqual(1, l.tail.data)
        l.add_tail(2)
        self.assertEqual(1, l.head.data)
        self.assertEqual(2, l.tail.data)

    def test_delete_head(self):
        l = LinkedListADT()
        l.add_tail(1)
        l.add_tail(2)
        self.assertEqual(1, l.head.data)
        self.assertEqual(2, l.tail.data)
        l.delete_head()
        self.assertEqual(2, l.head.data)
        self.assertEqual(2, l.tail.data)
        l.delete_head()
        self.assertEqual(None, l.head)
        self.assertEqual(None, l.tail)


    def test_delete_tail(self):
        l = LinkedListADT()
        l.add_tail(1)
        l.add_tail(2)
        self.assertEqual(1, l.head.data)
        self.assertEqual(2, l.tail.data)
        l.delete_tail()
        self.assertEqual(1, l.head.data)
        self.assertEqual(1, l.tail.data)
        l.delete_tail()
        self.assertEqual(None, l.head)
        self.assertEqual(None, l.tail)

    def test_count(self):
        l = LinkedListADT()
        self.assertEqual(0, l.count()) 
        l.add_tail(1)
        self.assertEqual(1, l.count()) 
        l.add_tail(2)
        self.assertEqual(2, l.count()) 
        l.delete_tail()
        self.assertEqual(1, l.count()) 
        l.delete_tail()
        self.assertEqual(0, l.count())

    def test_get_head(self):
        l = LinkedListADT()
        self.assertEqual(None, l.get_head()) 
        l.add_tail(1)
        self.assertEqual(1, l.get_head().data) 
        l.add_tail(2)
        self.assertEqual(1, l.get_head().data) 
        l.delete_tail()
        self.assertEqual(1, l.get_head().data) 
        l.delete_tail()
        self.assertEqual(None, l.get_head())

if __name__ == "__main__":
    unittest.main()