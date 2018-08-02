import time

class MergeSort:
    def __init__(self):
        self.name = "MergeSort"
        self.compare = 0


    def sort(self, data, cmp):
        """
        use cmp to sort data 
        cmp will take two elemenets x and y and return 
        True if x should go before y 
        """
        self.compare = 0
        if len(data) <= 1:
            return data
        m = len(data) // 2
        l1 = self.sort(data[:m], cmp)
        l2 = self.sort(data[m:], cmp)
        res = self.merge(l1, l2, cmp) 
        return res

    def merge(self, l1, l2, cmp):
        i = 0
        j = 0
        res = []
        while i < len(l1) and j < len(l2):
            if cmp(l1[i], l2[j]):
                self.compare += 1
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        
        while i < len(l1):
            res.append(l1[i])
            i += 1

        while j < len(l2):
            res.append(l2[j])
            j += 1
        
        return res
        