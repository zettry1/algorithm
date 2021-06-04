

#another idea is sort the list and get 0th value #O(nlogn)
#O(n)|O(1)
def find_minimum(arr):
    if len(arr)==0:
        return None

    min= float("Inf")
    for num in arr:
        min = min if  min<num else num
    return min


#


print(find_minimum([1,2,3,4,5,-100]))