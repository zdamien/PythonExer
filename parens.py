""" Two different functions for making sets of matched parentheses
"""
def yieldgen(n):
    """
>>> list(recgen(3))
['()()()', '(()())', '()(())', '((()))', '(())()']
"""
    if n<=1:
        yield '()'
        return  #needed to escape infinite loop
    for par in yieldgen(n-1):
        p1='()'+par
        p2='('+par+')'
        p3=par+'()'
        yield p1 
        yield p2 
        if p1 != p3:
            yield p3 


def recgen(n):
    """Recursive on strings
>>> recgen(1)
['()']
>>> recgen(2)
['()()', '(())']
>>> recgen(3)
['()()()', '(()())', '()(())', '((()))', '(())()']
>>> recgen(4) == list(yieldgen(4))
True
"""
    if n<=1:
        return ['()']
    l1 = recgen(n-1)
    l2=[]
    for par in l1:
        p1='()'+par
        p2='('+par+')'
        p3=par+'()'
        l2.append(p1)
        l2.append(p2)
        if p1 != p3:
            l2.append(p3)
    return l2

def pargen(n):
    """Recursive on parameters
>>> pargen(1)
()
>>> pargen(2)
(())
()()
>>> pargen(3)
((()))
(()())
(())()
()(())
()()()
"""
    if n<=0: return ''
    def parhelp(l,r,s):
        if l==0 and r==0: print(s)
        if r==0:
            parhelp(l-1,r+1,s+'(')
        elif l==0:
            print (s+')'*r)
        else:
            parhelp(l-1,r+1,s+'(')
            parhelp(l,r-1,s+')')
    parhelp(n,0,"")
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()


#pargen(1)
#print()
#pargen(2)
#print()
#pargen(3)
#print()
#pargen(4)
#print()
#print (recgen(1))
#print (recgen(2))
#print (recgen(3))


