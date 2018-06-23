"""
Arthor: Xinran Hu

Graph ADT unit test file
"""

#! python 

import unittest
from GraphADT import *

class TestGraph(unittest.TestCase):
    def test_init(self):
        g = GraphADT()
        g.create_graph(4)
        self.assertEqual(0, g.size)

    def test_printMatrix(self):
        g = GraphADT()
        g.create_graph(4)
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        g.add_edge(0, 1)
        g.add_edge(1, 0)
        g.add_edge(1, 2)
        print("")
        g.printMatrix()

    def test_add_vertex(self):
        g = GraphADT()
        g.create_graph(4)
        g.add_vertex()
        self.assertEqual(1, g.size)
        g.add_vertex()
        self.assertEqual(2, g.size)
        g.add_vertex()
        self.assertEqual(3, g.size)
    
    def test_remove_vertex(self):
        g = GraphADT()
        g.create_graph(4)
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        self.assertEqual(3, g.size)
        g.remove_vertex()
        self.assertEqual(2, g.size)
        g.remove_vertex()
        self.assertEqual(1, g.size)
        g.remove_vertex()
        self.assertEqual(0, g.size)


    def test_add_edge(self):
        g = GraphADT()
        g.create_graph(4)
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        g.add_edge(0, 1)
        self.assertEqual(True, g.adj[0][1])
        g.add_edge(1, 2)
        self.assertEqual(True, g.adj[1][2])
        g.add_edge(2, 0)
        self.assertEqual(True, g.adj[2][0])

    def test_remove_edge(self):
        g = GraphADT()
        g.create_graph(4)
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        
        g.remove_edge(0, 1)
        self.assertEqual(False, g.adj[0][1])
        g.remove_edge(1, 2)
        self.assertEqual(False, g.adj[1][2])
        g.remove_edge(2, 0)
        self.assertEqual(False, g.adj[2][0])
    
    def test_dfs(self):
        g = GraphADT()
        g.create_graph(4)
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        g.add_edge(0, 2)  
        g.add_edge(0, 1)
        g.add_edge(1, 0)
        g.add_edge(2, 3)
        g.add_edge(2, 0)
        g.add_edge(3, 1)
        v = g.dfs(2)
        self.assertEqual([2 ,0 , 1, 3], v)


if __name__ == "__main__":
    unittest.main()