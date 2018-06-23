"""
Author : Xinran Hu
"""

from LinkedListADT import *

class MiddleList:
    def __init__(self, data):
        self.list = LinkedListADT()
        for d in data:
            self.list.add_tail(d)
    
    def middle_list(self):
        fast = self.list.get_head()
        slow = self.list.get_head()
        while fast:
            fast = fast.next 
            if not fast:
                break
            fast = fast.next
            slow = slow.next
        return slow.data

def main():
    data = range(13)
    ml = MiddleList(data)
    n = ml.list.get_head()
    d = []
    while n:
        d.append(n.data)
        n = n.next
    print(d)
    print(ml.middle_list())

if __name__ == "__main__":
    main()