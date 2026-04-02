# Ques: using Newton roof was evaluate the evaluate the rooot of x sinx+cosx


import math

def f(x):
    return x*math.sin(x) + math.cos(x)

def df(x):
    return x*math.cos(x)

x0 = 2.5   

for i in range(10):
    x1 = x0 - f(x0)/df(x0)
    x0 = x1

    print("Root of the equation =", x1)