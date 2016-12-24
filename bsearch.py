def bsearch(arr, targ):
    """Standard binary search, with recursive or iterative subfunctions.
    Returns leftmost idnex of a value, or where a value would be if
    present.

>>> print(bsearch([1,1,2,4],1))
0
>>> print(bsearch([1,1,2,4],2))
2
>>> print(bsearch([1,1,2,4],3))
3
>>> print(bsearch([1,1,2,4],4))
3
>>> print(bsearch([1,1,2,4],5))
4
>>> print(bsearch([1,1],2))
2
>>> print(bsearch([4,5],6))
2
>>> print(bsearch([4,5],5))
1
>>> print(bsearch([4,5],4))
0
>>> print(bsearch([4,5],3))
0
>>> print(bsearch([3,5],4))
1
>>> print(bsearch([1,1],0))
0
>>> print(bsearch([1],1))
0
>>> print(bsearch([1],0))
0
>>> print(bsearch([1],2))
1
>>> print(bsearch([],0))
0
"""
    def _bsearch(left,right):
        #print(left, right)
        if left == right:
            return left
        else:
            mid = (left+right)//2
            if arr[mid] < targ:
                return _bsearch(mid+1, right)
            else:
                return _bsearch(left, mid)

    def _itsearch(left,right):
        while left < right:
            mid = (left+right)//2
            if arr[mid] < targ:
                left = mid+1
            else:
                right = mid
        return left
    return _itsearch(0, len(arr))



import doctest
if __name__ == "__main__":
    doctest.testmod()
