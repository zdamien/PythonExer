"""simple numerical integration code.  left and right Riemann sums,
mdpoint Riemann, and something of my own: value of a strip is
(f(left)+f(right))/2, over all streips that becomes f(a)/2 + f(b)/2 +
f(b)/2 + f(c)/2 + f(c/2)... +f(y)/2 + f(z)/2
So it simply sums up f(b)...f(y), and adds half of f(a) and f(z)
Conlcusion: it by far beats the first two, but is less accurate than the
ussual midpoint sum.
"""

import math

def left(f, start, end, cols):
    acc=0
    step = (end-start)/cols
    x=start
    for i in range(cols):
        acc += f(x)*step
        x += step
    return acc

def right(f, start, end, cols):
    acc=0
    step = (end-start)/cols
    x=start+step
    for i in range(cols):
        acc += f(x)*step
        x += step
    return acc

def mid(f, start, end, cols):
    acc=0
    step = (end-start)/cols
    half = step/2
    x=start+half
    for i in range(cols):
        acc += f(x)*step
        x += step
    return acc

def odd(f, start, end, cols):
    acc=0
    step = (end-start)/cols
    x=start+step
    for i in range(cols-1):
        acc += f(x)*step
        x += step
    acc += (f(start)+f(end))*step/2
    return acc


def main():
    def ff(x):
        return math.sin(x)

    start=0
    end=math.pi/2
    step = 1000

    print(left(ff,start,end,step))
    print(right(ff,start,end,step))
    print(mid(ff,start,end,step))
    print(odd(ff,start,end,step))

main()
    
