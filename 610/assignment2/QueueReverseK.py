"""
Author : Xinran Hu
"""

from StackADT import *
from QueueADT import *

class QueueReverseK:
    def reverseK(self, q, k):
        qMod = QueueADT(q.size())
        qTemp = QueueADT(q.size())
        sTemp = StackADT()
        i = 0
        while not q.is_empty():
            n = q.dequeue()
            if i < k:
                sTemp.push(n)
            else:
                qTemp.enqueue(n)
            i += 1
        
        while not sTemp.is_empty():
            qMod.enqueue(sTemp.pop())
        
        while not qTemp.is_empty():
            qMod.enqueue(qTemp.dequeue())
        
        return qMod


if __name__ == "__main__":
    data = [12, 34, 65, 76, 23, 12, 36, 90]
    qOri = QueueADT(len(data))
    for d in data:
        qOri.enqueue(d)
    algo = QueueReverseK()
    qMod = algo.reverseK(qOri, 4)
    data_mod = []
    while not qMod.is_empty():
        data_mod.append(qMod.dequeue())
    
    print("Original", data)
    print("Reversed", data_mod)