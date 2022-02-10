
# This file passes a function as a formal parameter

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def fn(x, y, f):
    return "f(n) is " + str(f(x,y))

def astar_search(g, h):
    return g + h

def ucs_search(g, h):
    return g

def greedy_search(g, h):
    return h


if __name__ == '__main__':
    print(fn(8, 4, add)) # passing in a function name so our fn function's formal parameter f can use this operation!
    print()
    print(fn(8, 4, sub))
    print()
    print(fn(8, 4, mul))
    
    