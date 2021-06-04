def rearrange(lst):
    arranged_list=[]
    for num in lst:
        if num <0:
            arranged_list.append(num)
    for num in lst:
        if num >=0:
            arranged_list.append(num)
    return arranged_list


# Rearraning in place
#O(n)|O(1)
def rearrange_2(lst):
    leftMostPosEle = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            if i is not leftMostPosEle:
                print(i,leftMostPosEle)
                lst[i], lst[leftMostPosEle] =lst[leftMostPosEle] ,lst[i]
            leftMostPosEle+=1
    return lst


#O(n)|O(n)
def rearrange_3(lst):
    return [i for i in lst if i<0] + [i for i in lst if i >= 0]


print(rearrange_2([10, -1, 20, 4, 5, -9, -6]))