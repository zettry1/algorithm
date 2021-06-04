#O(n)|O(n)
def max_min(lst):
    result=[]

    for i in range(len(lst)//2):
        result.append(lst[-(i+1)])

        result.append(lst[i])

    if len(lst)%2==1:
        result.append(lst[len(lst)//2])
    return result


def max_min2(lst):
    if len(lst) is 0:
        return []

    maxIdx = len(lst)-1
    minIdx = 0
    maxElm = lst[-1] +1
    print(lst)
    for i in range(len(lst)):
        if i%2==0:
            lst[i]+=(lst[maxIdx] % maxElm) * maxElm
            print('event',lst[i])
            maxIdx-=1
        else:
            print('odd',(lst[minIdx] % maxElm) * maxElm)
            lst[i] += (lst[minIdx] % maxElm) * maxElm
            minIdx+=1
    for i in range(len(lst)):
        lst[i] = lst[i] // maxElm
    return lst

print(max_min2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))