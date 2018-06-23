#! python
import math

def method1(x, n):
    truth = math.exp(-x)
    res = [0.0]
    total = 0.0
    for i in range(n + 1):
        term = pow(-x, i) / math.factorial(i)
        total += term
        res.append(total)
        ae = abs((truth - res[-1]) / truth)
        re = abs(term / res[-1])
        print("term : {} | true rel err {:0.1%} | apprx rel err {:0.1%}".format(i, ae, re))
    return res

def method2(x, n):
    truth = math.exp(-x)
    res = [0.0]
    total = 0.0
    for i in range(n + 1):
        term = pow(x, i) / math.factorial(i)
        total += term
        res.append(1 / total)
        ae = abs((truth - res[-1]) / truth)
        re = abs(term / res[-1])
        print("term : {} | true rel err {:0.1%} | apprx rel err {:0.1%}".format(i, ae, re))
    
    return res

def main():
    t = 20
    print("method1")
    method1(5, t)
    print("="  * 40)
    
    print("method2")
    method2(5, t)


if __name__ == "__main__":
    main()

