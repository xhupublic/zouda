class NQueen:
    def __init__(self, n):
        self.n = n
        self.col = [0] * (n + 1)
        self.solutions = []

    def print_board(self):
        print(self.solutions)   
        print(len(self.solutions))

    def promising(self, i):
        for j in range(1, i):
            if self.col[j] == self.col[i]:
                return False
            if abs(self.col[i] - self.col[j]) == (i - j):
                return False
        return True


    def queen(self, i):
        if not self.promising(i):
            return 
        
        if i == self.n:
            self.solutions.append(self.col[1:])
            return
        
        for j in range(self.n):
            self.col[i + 1] = j
            self.queen(i + 1)
        

for i in [13]:
    N = NQueen(i)
    N.queen(0)
    print(len(N.solutions))