"""Edit distance problem, a la the dynamic programming chapter of
Skiena.  Memoized recursive forms.  Variant functions to experiment with
speed."""

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

#notably slower than _string, like .3s vs. .2 on n=200
# or 1 to 0.5 on 400
def editwrap_concise(s1,s2,l1,l2):
    import functools
    @functools.lru_cache(maxsize=None)
    def edithelp(a,b):
        dists=['']*3  # 0.04 seconds on n=400 this way
        paths=['']*3  # 0.04 seconds on n=400 this way
        if a==-1: return b+1,'I'*(b+1)
        if b==-1: return a+1,'D'*(a+1)

        temp,tpath=edithelp(a-1, b-1)
        choice='m'
        if s1[a]!=s2[b]: 
            temp+=1
            choice='S'
        #dists[0]=temp,tpath,choice  #save 0.03 seconds
        dists[0]=temp
        paths[0]=tpath,choice
        #dists.append((temp,tpath+choice))

        temp,tpath=edithelp(a,b-1) #insert
        dists[1]=temp+1
        paths[1]=tpath,'I'
        #dists[1]=temp+1,tpath,'I'
        #dists.append((temp+1,tpath+'I'))

        temp,tpath=edithelp(a-1,b) #delete
        dists[2]=temp+1
        paths[2]=tpath,'D'
        #dists[2]=temp+1,tpath,'D'
        #dists.append((temp+1,tpath+'D'))

        #opt=min(dists)
        ind=0  # saved 0.06 seconds!
        if dists[1]<dists[0]: ind=1
        if dists[2]<dists[ind]: ind=2
        opt=dists[ind]
        #ind=dists.index(opt)  # now 0.84 s
        #opt=min(dists, key=lambda x: x[0])
        return opt,paths[ind][0]+paths[ind][1]
        #return opt[0],opt[1]+opt[2]
    dist,pathlist = edithelp(l1,l2)
    return dist, pathlist

def editwrap_simple(s1,s2,l1,l2):
    """Just calculates distance
    """
    import functools
    @functools.lru_cache(maxsize=None)
    def edithelp(a,b):
        if a==-1: return b+1
        if b==-1: return a+1
        opt=edithelp(a-1, b-1)
        if s1[a]!=s2[b]: 
            opt+=1
        temp=edithelp(a,b-1) #insert
        temp+=1
        if temp<opt: 
            opt=temp
        temp=edithelp(a-1,b) #delete
        temp+=1
        if temp<opt: 
            opt=temp
        return opt
    dist = edithelp(l1,l2)
    return dist
 
def editwrap_string(s1,s2,l1,l2):
    """The original version, correct and fastest
    """
    import functools
    @functools.lru_cache(maxsize=None)
    def edithelp(a,b):
        #if a==-1 and b==-1: return 0,[""]
        if a==-1: return b+1,'I'*(b+1)
        if b==-1: return a+1,'D'*(a+1)
        opt,path=edithelp(a-1, b-1)
        #print(opt,path)
        choice='m'
        if s1[a]!=s2[b]: 
            opt+=1
            choice='S'
        path+=(choice)
        temp,tpath=edithelp(a,b-1) #insert
        temp+=1
        if temp<opt: 
            opt=temp
            choice='I'
            tpath+=(choice)
            path=tpath
        temp,tpath=edithelp(a-1,b) #delete
        temp+=1
        if temp<opt: 
            opt=temp
            choice='D'
            tpath+=(choice)
            path=tpath
        return opt, path
    dist,pathlist = edithelp(l1,l2)
    #print (dist,pathlist)
    #return dist, pathlist
    return dist, pathlist

def editwrap_list(s1,s2,l1,l2):
    """ attempt to speed up... failed; takes much longer than string
    version
    """
    import functools
    @functools.lru_cache(maxsize=None)
    def edithelp(a,b):
        #if a==-1 and b==-1: return 0,[""]
        if a==-1: return b+1,['I']*(b+1)
        if b==-1: return a+1,['D']*(a+1)
        opt=99999999999
        path=[]
        temp,tpath=edithelp(a-1, b-1)
        #print(' '*n,'m/s',temp,tpath)
        choice='m'
        if s1[a]!=s2[b]: 
            temp+=1
            choice='S'
        if temp<opt:
            opt=temp
            path=tpath

        temp,tpath=edithelp(a,b-1) #insert
        #print(' '*n,'ins',temp,tpath)
        temp+=1
        if temp<opt: 
            opt=temp
            choice='I'
            path=tpath

        temp,tpath=edithelp(a-1,b) #delete
        #print(' '*n,'del',temp,tpath)
        temp+=1
        if temp<opt: 
            opt=temp
            choice='D'
            path=tpath
        path=path+[choice]
        return opt, path
    dist,pathlist = edithelp(l1,l2)
    #print ('final',dist,pathlist)
    #return dist, pathlist
    return dist, "".join(pathlist)
        
def editdist(s1,s2):
    """
>>> editdist('ccc','')
(3, 'DDD')
>>> editdist('ccc','ddd')
(3, 'SSS')
>>> editdist('','ddd')
(3, 'III')
>>> editdist('','')
(0, '')
>>> editdist('a','a')
(0, 'm')
>>> editdist('a','b')
(1, 'S')
>>> editdist('a','ba')
(1, 'Im')
>>> editdist('a','ab')
(1, 'mI')
>>> editdist('a','aba')
(2, 'IIm')
>>> editdist('aba','a')
(2, 'DDm')
>>> editdist('aab','a')
(2, 'DmD')
>>> editdist('Gregory', ' Gregorian')
(4, 'ImmmmmmIIS')
>>> editdist('bcaaa','aaaa')
(2, 'DSmmm')
>>> editdist('abc','defacb')
(5, 'IIImSS')
>>> editdist('Gr abace g',' Gr aaffg')
(5, 'ImmmmDmDSSm')
>>> editdist('ck','acake')
(3, 'ImImI')
"""
    return editwrap_string2(s1,s2,len(s1)-1,len(s2)-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

sys.setrecursionlimit(10**6)
#s1,s2="the old man said, Alice: when I was young end layed, Fourscore and seven years ago","the old woman said, Bob: Alice, I played foursquare for many years"
#s1, s2="allthere ZZ cat", "...there cats"
N=500
s1, s2='a'*N, 'b'*N
print(editdist(s1,s2))
