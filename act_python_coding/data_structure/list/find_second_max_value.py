

#O(nlogn)|O(1)
def find_second_maximum(lst):
    lst.sort()
    if len(lst)>=2:
        return lst[-2]
    else:
        return None

#O(n)|O(1)
def find_second_maximum2(lst):
    first_max=float("-inf")
    second_max = float("-inf")

    for item in lst:
        if item> first_max:
            first_max=item
    for item in lst:
        if item!=first_max and item>second_max:
            second_max=item
    return second_max


#O(n)|O(1)
def find_second_maximum3(lst):
    if len(lst)<2:
        return
    max_no = second_max_no = float("-inf")
    for i in range(len(lst)):
        if (lst[i]>max_no):
            second_max_no = max_no
            max_no = lst[i]
        elif (lst[i]> second_max_no and lst[i]!=max_no):
            print('cane here once')
            second_max_no = lst[i]
        print(max_no,second_max_no)
    if (second_max_no == float('-inf')):
        return
    else:
        return second_max_no



print(find_second_maximum3([1,2,4,4,6,7,7]))