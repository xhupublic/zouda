#! python
"""
Xinran

BST implementation with in order range function
"""

import random

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)

    def find(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left:
                return self.left.find(val)
            else:
                return False
        else:
            if self.right:
                return self.right.find(val)
            else:
                return False
    
    def delete(self, val):
        if val == self.val:
            if self.left is None:
                return self.right

            n = self.left
            while n.right:
                n = n.right
            n.right = self.right
            return self.left  
        elif val < self.val:
            if self.left:
                self.left = self.left.delete(val)
                return self
        else:
            if self.right:
                self.right = self.right.delete(val)
                return self
    
    def in_order_range(self, i, j):
        
        if self.left and self.val >= i:
            self.left.in_order_range(i, j)

        if i <= self.val and self.val <= j:
            print(self.val)

        if self.right and self.val < j: 
            self.right.in_order_range(i, j)

    def in_order(self):
        if self.left:
            self.left.in_order()
        
        print(self.val)

        if self.right: 
            self.right.in_order()



class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = Node(val)
        
    def find(self, val):
        if not self.root:
            return False
        else:
            return self.root.find(val)
    
    def delete(self, val):
        if not self.root:
            return
        else:
            self.root = self.root.delete(val)

    def in_order(self):
        if self.root:
            self.root.in_order()
    
    def in_order_range(self, i, j):
        if self.root:
            self.root.in_order_range(i, j)
    

def main():
    T = BST()
    data = [21, 38, 40, 45, 50, 86, 90]
    for d in data:
        T.insert(d)
    print("in order before deletion")
    T.in_order()

    
    print("found 21 : ", T.find(21))
    print("found 38 : ", T.find(38))
    print("found 39 : ", T.find(39))

    print("deleting 38")
    T.delete(38)
    
    print("in order after deleting 38")
    T.in_order()

    print("in order range bewteen 40 and 80")
    T.in_order_range(40, 80)



if __name__ == "__main__":
    main()
