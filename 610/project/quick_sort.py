"""
implementation of quick sort
"""
import time
class QuickSort:
    def __init__(self):
        self.name = "QuickSort"
        self.compare = 0
        
    def sort(self, data, cmp):
        self.compare = 0
        self.quick_sort(data, cmp, 0, len(data) - 1)
        return data

    def quick_sort(self, data, cmp, i, j):
        if i >= j:
            return
        k = self.partition(data, cmp, i, j)
        self.quick_sort(data, cmp, i, k - 1)     
        self.quick_sort(data, cmp, k + 1, j)

    def partition(self, data, cmp, i, j):
        pivot = data[j]
        k = i
        while i < j:
            if cmp(data[i], pivot):
                self.compare += 1
                data[k], data[i] = data[i], data[k]
                k += 1
            i += 1
        data[k], data[j] = data[j], data[k]
        return k
