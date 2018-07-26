class NQueen:
    def __init__(self, n):
        self.n = n
        self.col = [0] * (n + 1)
        self.solutions = []

    def save_board(self):
        with open("nqueen_solution_n={}.txt".format(self.n), "w") as f:
            f.write("{} solutions for n = {}\n".format(len(self.solutions), self.n))
            for s in self.solutions:
                f.write("{}\n".format(str(s)))
                f.flush()

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

def main():
    for i in [4, 11, 13]:
        N = NQueen(i)
        N.queen(0)
        N.save_board()
        print("{} solutions for n = {}".format(len(N.solutions), i))

if __name__ == "__main__":
    main()