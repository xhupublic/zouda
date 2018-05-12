import unittest
from StackADT import *

class TestQueue(unittest.TestCase):
    def test_init(self):
        s = StackADT()
    
    def test_is_empty(self):
        s = StackADT()
        self.assertEqual(True, s.is_empty())
        s.push(1)
        self.assertEqual(False, s.is_empty())
        s.push(2)
        self.assertEqual(False, s.is_empty())
        s.pop()
        self.assertEqual(False, s.is_empty())
        s.pop()
        self.assertEqual(True, s.is_empty())

    def test_push(self):
        s = StackADT()
        s.push(1)
        s.push(2)
        
    def test_pop(self):
        s = StackADT()
        s.push(1)
        s.push(2)
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())

    def test_size(self):
        s = StackADT()
        self.assertEqual(0, s.size())
        s.push(1)
        self.assertEqual(1, s.size())
        s.push(2)
        self.assertEqual(2, s.size())
        s.pop()
        self.assertEqual(1, s.size())
        s.pop()
        self.assertEqual(0, s.size())
        

if __name__ == "__main__":
    unittest.main()