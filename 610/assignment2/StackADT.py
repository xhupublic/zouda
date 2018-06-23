"""
Author : Xinran Hu
"""
from LinkedListADT import *

class StackADT:
    def __init__(self):
        self.items = LinkedListADT()

    def is_empty(self):
        return self.items.get_head() == None

    def pop(self):
        n = self.items.get_head().data
        self.items.delete_head()
        return n

    def push(self, item):
        self.items.add_head(item)

    def size(self):
        return self.items.count()