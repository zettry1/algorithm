def pivoted_binary_search(lst,n,key):

    pivot = find_pivot_point(lst,0,n-1)

    if pivot ==-1:
        return binary_search(lst,0,n-1,key)

    if lst[pivot] == key:
        return pivot

    if lst[0] <=key:
        return binary_search(lst,0,pivot-1,key)
    return binary_search(lst,pivot+1,n-1,key)


def find_pivot_point(lst,low,high):
    if high<low:
        return -1

    if high ==low:
        return low

    mid = (low+high)//2

    if mid < high and lst[mid] > lst[mid+1]:
        return mid

    if mid > low and lst[mid] < lst[mid-1]:
        return mid-1

    if lst[low]>= lst[mid]:
        return find_pivot_point(lst,low,mid-1)

    return find_pivot_point(lst,mid+1,high)

def binary_search(lst,low,high,key):

    if high < low:
        return -1

    mid = (low+high)//2

    if key == lst[mid]:
        return mid

    if key> lst[mid]:
        return binary_search(lst,mid+1,high,key)

    return binary_search(lst,low,mid-1,key)


if __name__ =="__main__":
    lst = [6, 7, 8, 9, 10, 0, 1, 2, 3]
    key = 0

    print("Index:",pivoted_binary_search(lst,len(lst),key))
