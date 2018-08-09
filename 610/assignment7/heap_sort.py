class Heap:
    def __init__(self, data, cmp=lambda x, y : x < y):
        self.data = [x for x in data]
        self.n = len(data)
        self.cmp = cmp


    def __repr__(self):
        return "{}|{}".format(self.n, self.data)

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
        print("called")
        for i in range(int(self.n / 2), -1, -1):
            self.siftdonw(i)
        

class HeapSort:    
    def __init__(self):
        pass

    def make_heap(self):
        pass

    def sort(self, data, cmp):
        pass



d = [3, 2, 7, 4, 5, 6, 1]
h = Heap(d)
h.heapify()
print(h)