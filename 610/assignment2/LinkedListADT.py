class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListADT:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:        
            n.next = self.head
            self.head = n

    def add_tail(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:      
            self.tail.next = n
            self.tail = n

    def delete_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next


    def delete_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        n = self.head
        while n.next != self.tail:
            n = n.next
        self.tail = n
        self.tail.next = None


    def count(self):
        n = self.head
        size = 0
        while n:
            n = n.next
            size += 1
        return size


    def get_head(self):
        return self.head
