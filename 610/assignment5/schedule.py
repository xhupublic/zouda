#! python


jobs = [
(1, 2, 65), 
(2, 3, 50), 
(3, 2, 47), 
(4, 3, 32), 
(5, 4, 30),
(6, 2, 15),
(7, 1, 10)
]

def main():
    max_time = 0
    for j in jobs:
        max_time = max(j[1], max_time)

    taken = [None] * max_time
    for j in jobs:
        can_take = False
        for i in reversed(range(j[1])):
            if taken[i] is None:
                taken[i] = j
                can_take = True
                print("take", j, "at ", i)
                break
        if not can_take:
            print("can not take", j)
    print(taken)
    s = 0
    for t in taken:
        if t:
            s += t[2]
    print("total", s) 


if __name__ == "__main__":
    main()