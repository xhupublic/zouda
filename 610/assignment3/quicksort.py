#! python
"""
Xinran Hu

Quick sort implementation
"""
import time
from collections import defaultdict
import sys
sys.setrecursionlimit(15000)

class Quicksort:
    def quicksort(self, data):
        self.quicksort_helper(data, 0, len(data) - 1)

    def quicksort_helper(self, data, i, j):
        if i >= j:
            return
        k = self.quickpartition(data, i, j)
        self.quicksort_helper(data, i, k - 1)
        self.quicksort_helper(data, k + 1, j)

    def quickpartition(self, data, i, j):
        s = i
        for f in list(range(i, j)):
            if data[f] < data[j]:
                data[s], data[f] = data[f], data[s]
                s += 1 
        data[s], data[j] = data[j], data[s]
        return s

#! python

import random

def sorted_data(n):
    return list(range(int(n)))

def reverse_data(n):
    return list(range(int(n), 1, -1))

def random_data(n):
    data = list(range(int(n)))
    random.shuffle(data)
    return data

def partially_sorted(n):
    p1 = random_data(int(n/2))
    p2 = sorted_data(int(n - n/2))
    data = []
    for i in range(int(n/2)):
        data.append(p1[i])
        data.append(p2[i])
    if i < n - n/2:
        data.append(p2[i])
    return data

def main():
    Q = Quicksort()
    data = [3, 2, 1, 4, 5]
    print("before", data)
    Q.quicksort(data)
    print("after ", data)


    total_time = defaultdict(lambda: defaultdict(float)) 
    for n in [500, 1000, 2000]:
        t = 10
        for i in range(t):
            data = random_data(n)    
            s = time.time()
            Q.quicksort(data)
            total_time["random"][n] += time.time() - s
            
            data = sorted_data(n)
            s = time.time()
            Q.quicksort(data)
            total_time["sorted"][n] += time.time() - s

            data = partially_sorted(n)
            s = time.time()
            Q.quicksort(data)
            total_time["partiall_sorted"][n] += time.time() - s

            data = reverse_data(n)
            s = time.time()
            Q.quicksort(data)
            total_time["reverse_data"][n] += time.time() - s

    for k, v in total_time.items():
        for k1, v1 in v.items():
            print("type {}, size {}, avg sort time {:4.4f}".format(k, k1, int(v1 / t * 1e9)))


if __name__ == "__main__":
    main()