#! python
"""
Author: Xinran Hu

Knapsack Implementation
"""


import queue

class Node:
  def __init__(self, value=0):
    self.value = value
    self.level = 0
    self.profit = 0
    self.weight = 0
    self.bound = 0

  def __repr__(self):
    return "level={}, wt={}, profit={}, bound={}".format(
        self.level, self.weight, self.profit, self.bound)

  def __eq__(self, other):
    return self.value == other.value

  def __lt__(self, other):
    return self.value > other.value

class Knapsack:

  def __init__(self, n, p, w, W):
    self.n = n
    self.p = p 
    self.w = w 
    self.W = W
    self.profit = 0
    self.weight = 0
    self.maxprofit = 0
    self.include = [False] * (n + 1)

  def promising(self, i, profit, weight):
    if weight > self.W:
      return False
  
    totalweight = weight
    bound = profit
    j = i + 1
    while j <= self.n and totalweight + self.w[j] < self.W:
      totalweight += self.w[j]
      bound += self.p[j]
      j += 1
    
    k = j
    if k <= self.n:
      bound += (self.W - totalweight) * self.p[k] / self.w[k]
    return bound > self.maxprofit
  
  def knapsack(self, i, profit, weight):
    if weight < self.W and profit > self.maxprofit:
      self.maxprofit = profit
      self.bestset = self.include
    
    if self.promising(i, profit, weight):
      print("level=", i, "wt=",  weight, "profit=", profit, " is promising")
      self.include[i + 1] = True
      self.knapsack(i + 1, profit + self.p[i + 1], weight + self.w[i + 1])
      self.include[i + 1] = False
      self.knapsack(i + 1, profit, weight)
    else:
      print("level=", i, "wt=",  weight, "profit=", profit, " is not promising")
      
  def a57(self):
    self.knapsack(0, 0, 0)
    print("max profit = ", self.maxprofit)
    print("*" * 40)

  def bound(self, v):
    if v.weight > self.W:
      return 0
    
    result = v.profit
    totalweight = v.weight
    j = v.level + 1
    while j <= self.n and totalweight + self.w[j] < self.W:
      totalweight += self.w[j]
      result += self.p[j]
      j += 1

    k = j
    if k <= self.n:
      result += (self.W - totalweight) * self.p[k] / self.w[k]

    return result

  def a62(self):
    q = queue.PriorityQueue()
    v = Node()
    v.bound = self.bound(v)
    q.put(v)
    maxprofit = 0
    
    while q.qsize() > 0:
      v = q.get()

      
      if v.bound > maxprofit and v.level < self.n:
        print(v, "is promising")
        u = Node()
        u.level = v.level + 1
        u.weight = v.weight + self.w[u.level]
        u.profit = v.profit + self.p[u.level]
        
        if u.weight < self.W and u.profit > maxprofit:
          maxprofit = u.profit
        
        u.bound = self.bound(u)
        if u.bound > maxprofit:
          q.put(u)
        
        u = Node()
        u.level = v.level + 1
        u.weight = v.weight
        u.profit = v.profit
        u.bound = self.bound(u)
        if u.bound > maxprofit:
          q.put(u)
      else:
        print(v, "is not promising")
    print("max profit = ", maxprofit)
    print("*" * 40)
    return maxprofit


def main():
  n = 3
  p = [0, 40, 45, 35]
  w = [0, 4, 5, 5]
  W = 12
  k = Knapsack(n, p, w, W)
  k.a57()
  k.a62()

if __name__ == "__main__":
  main()