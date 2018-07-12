"""
Arthor: Xinran Hu

Graph ADT implementation with adj matrix
"""

class Vertex:
    def __init__(self, label=None):
        self.label = label   


class GraphADT:
    def __init__(self):
        self.size = 0
        self.max = 0
        self.adj = None
        self.vertices = []

    def create_graph(self, _max):
        self.size = 0
        self.max = _max
        self.adj = [[False for i in range(_max)] for j in range(_max)]
        

    def add_vertex(self, label=None):
        if self.size < self.max:
            self.vertices.append(Vertex(label))
            self.size += 1
            return True
        else:
            return False

    def remove_vertex(self):
        if self.size > 0:
            self.vertices.pop()
            self.size -= 1
            return True
        else:
            return False

    def add_edge(self, f, t):
        if f >= self.size or t >= self.size:
            return False
        else:
            self.adj[f][t] = True
            return True
    

    def remove_edge(self, f, t):
        if f >= self.size or t >= self.size:
            return False
        else:
            self.adj[f][t] = False
            return True

    def append_cell(self, s, data=""):
        return s + "{:>6s} ".format(str(data))

    def printMatrix(self):
        s = "\n" 
        s = self.append_cell(s)
        for i in range(self.size):
            s = self.append_cell(s, i)
        s = self.append_cell(s, "\n")
        for i in range(self.size):
            s = self.append_cell(s, i)
            for j in range(self.size):
                s = self.append_cell(s, self.adj[i][j])
            s = self.append_cell(s, "\n")
        s = self.append_cell(s, "\n")
        print(s)

    def dfs(self, n):
        visited = []
        self.dfs_helper(n, visited)
        return visited

    def dfs_helper(self, n, visited):
        visited.append(n)
        for i in range(self.size):
            if self.adj[n][i] and i not in visited:
                self.dfs_helper(i, visited)
