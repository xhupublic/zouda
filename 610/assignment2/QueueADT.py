class QueueADT:
    def __init__(self, _max):
        self.items = [None] * _max
        self.max = _max
        self.end = 0

    def is_empty(self):
        return self.end == 0
    
    def is_full(self):
        return self.end >= self.max
    
    def enqueue(self, item):
        if self.is_full():
            raise("queue is full")
        self.items[self.end] = item
        self.end += 1
    
    def dequeue(self):
        if self.is_empty():
            raise("queue is empty")
        n = self.items[0]
        for i in range(1, self.end):
            self.items[i - 1] = self.items[i]
        self.end -= 1
        return n
        
    def size(self):
        return self.end
