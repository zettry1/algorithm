#O(n)|O(n)
def right_rotate(lst,k):
    if len(lst) ==0:
        k=0
    else:
        k=k% len(lst)
    rotatedList=[]
    for i in range(len(lst)-k,len(lst)):
        rotatedList.append(lst[i])
    for i in range(0,len(lst)-k):
        rotatedList.append(lst[i])
    return rotatedList


def right_rotate2(lst,k):
    if (len(lst)==0):
        k=0
    else:
        k=k %len(lst)
    return lst[-k:]+lst[:-k]

print(right_rotate2([10,20,30,40,50,60,70,80],3))