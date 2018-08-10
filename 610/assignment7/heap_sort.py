#! python3
"""
heapsort implementation

Xinran Hu
"""

class Heap:
    def __init__(self, data, cmp):
        self.data = [x for x in data]
        self.n = len(data)
        self.cmp = cmp

    def siftdonw(self, i):
        if i < 0 or i >= self.n:
            return
        
        swap = i
        l = i * 2 + 1
        r = i * 2 + 2
        if l < self.n and self.cmp(self.data[swap], self.data[l]):
            swap = l

        if r < self.n and self.cmp(self.data[swap], self.data[r]):
            swap = r
                
        if swap != i:
            self.data[i], self.data[swap] = self.data[swap], self.data[i]
            self.siftdonw(swap)

    
    def heapify(self):
        for i in range(int(self.n / 2), -1, -1):
            self.siftdonw(i)
        
        

class HeapSort:    
    def sort(self, data, cmp=lambda x, y : x < y):
        h = Heap(data, cmp)
        h.heapify()
        while h.n > 1:
            h.data[0], h.data[h.n - 1] = h.data[h.n - 1], h.data[0]
            h.n -= 1
            h.heapify()

        return h.data




d = [3, 2, 7, 4, 5, 6, 1]
h = HeapSort()
e = h.sort(d, lambda x, y : x > y)
print(d)
print(e)
heap_sort.py (END)
