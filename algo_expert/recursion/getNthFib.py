
def getNthFib(n,memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1,memoize)+getNthFib(n-2,memoize)
        return memoize[n]

#O(n)|O(1)
def getNFib2(n):
    sums=[0,1]
    counter=3
    while counter<=n:
        nextFeb = sums[0]+sums[1]
        sums[0] = sums[1]
        sums[1]= nextFeb
        counter+=1
    return sums[1] if n > 1 else sums[0]



print(getNFib2(8))