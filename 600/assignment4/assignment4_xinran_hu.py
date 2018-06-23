#!python
import math

"""
Question 4.2 
"""


def term(x, n):
    res = math.pow(-1 * x * x, n) / math.factorial(2 * n)
    return res

def cos(x):
    truth = math.cos(x)
    estimate = 0
    n = 0
    new_term = term(x, n)
    estimate += new_term
    true_err = abs((truth - estimate) / truth * 100)
    app_err = abs(new_term / estimate * 100)
    print("{} | estimate = {:4.4f}, true pct err {:4.4f}%, app pct err {:4.4f}%".format(n, estimate, true_err, app_err))
        
    while abs(app_err / estimate) >= 0.01:
        n += 1
        new_term = term(x, n)
        estimate += new_term
        true_err = abs((truth - estimate) / truth * 100)
        app_err = abs(new_term / estimate * 100)
        print("{} | estimate = {:4.4f}, true pct err {:4.4f}%, app pct err {:4.4f}%".format(n, estimate, true_err, app_err))    
    



if __name__ == "__main__":
    cos(math.pi / 3)