
#! python

import numpy as np  
import matplotlib.pyplot as plt
"""

"""

"""
"""
#def f(x):
#    return -25 + 82 * x - 90 * x ** 2 + 44 * x ** 3 - 8 * x ** 4 + 0.7 * x ** 5

def f(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6.1

def g(x):
    return 3 * x ** 2 - 12 * x + 11

def nr(f, g, x0, iter):
    i = 0
    while i < iter:
        x0 = x0 - f(x0) / g(x0)
        i += 1
        print(i, x0)
    return x0

def sec(f, x0, x1, iter):
    i = 0
    while i < iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2 
        i += 1
        print(i, x0)
    return x2

def sec_adj(f, x0, lam, iter):
    i = 0
    while i < iter:
        x1 = x0 * (1 + lam)
        x0 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)) 
        i += 1
        print(i, x0)
    return x0

def graphic(x):
    y = [f(x_i) for x_i in x]
    zeros = [0 for x_i in x]
    plt.plot(x, y)
    plt.plot(x, zeros)
    print(x, y)
    plt.show()

def bisec(l, r, e, f):
    error = 1
    old_root = 0
    i = 1
    while error * 100 > e:
        new_root = (l + r) / 2 
        print(i, new_root)
        i += 1
        if f(new_root) == 0:
            break
        elif f(new_root) * f(l) < 0:
            r = new_root
        else:
            l = new_root
        
        error = abs((new_root - old_root) / new_root)
        old_root = new_root
    return new_root

def fp(l, r, e, f):
    error = 1
    old_root = 0
    i = 0
    while error * 100 > e:
        new_root = l + f(r) * (l - r) / (f(l) - f(r))
        print(i, new_root)
        i += 1
        if f(new_root) == 0:
            break
        elif f(new_root) * f(l) < 0:
            r = new_root
        else:
            l = new_root
        
        error = abs((new_root - old_root) / new_root)
        old_root = new_root
    return new_root

if __name__ == "__main__":
    """
    graphic(np.linspace(-10, 10, 100))
    graphic(np.linspace(0, 5, 100))
    graphic(np.linspace(0.5, 3.5, 100))
    """
    print(nr(f, g, 3.5, 3))
    print(sec(f, 2.5, 3.5, 3))
    print(sec_adj(f, 3.5, 0.01, 3))
    

    
    """
    print(bisec(0.5, 1.0, 10, f))
    print(fp(0.5, 1.0, 0.2, f))
    graphic(np.linspace(-3, 5, 100))
    graphic(np.linspace(-1, 2, 100))
    """






