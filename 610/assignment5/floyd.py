#! python
"""
Author: Xinran Hu

Floyd Algorithm implementation
"""

import copy

class Floyd:

    @staticmethod
    def floyd2(n, W, D, P):
        for i in range(n):
            for j in range(n):
                P[i][j] = 0
                D[i][j] = W[i][j]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if D[i][k] + D[k][j] < D[i][j]:
                        P[i][j] = k
                        D[i][j] = D[i][k] + D[k][j]
        print("ret", D)

    @staticmethod
    def path(P, q, r):
        if P[q][r] != 0:
            Floyd.path(P, q, P[q][r])
            print(P[q][r])
            Floyd.path(P, P[q][r], r)



    @staticmethod
    def create_2d_array(n, v=None):
       return [[v for i in range(n)] for j in range(n)]

def main():

    W = Floyd.create_2d_array(5, float('Inf'))
    W[0][0] = 0
    W[0][1] = 1
    W[0][3] = 1
    W[0][4] = 5
    
    W[1][1] = 0
    W[1][0] = 9
    W[1][2] = 3
    W[1][3] = 2
    
    W[2][2] = 0
    W[2][3] = 4
    
    W[3][2] = 2
    W[3][3] = 0
    W[3][4] = 3
    
    W[4][0] = 3
    W[4][4] = 0
    
    D = Floyd.create_2d_array(5, 0)
    P = Floyd.create_2d_array(5, 0)
    Floyd.floyd2(5, W, D, P)
    print(D[4][0])
    Floyd.path(P, 4, 0)    


if __name__ == "__main__":
    main()