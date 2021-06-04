
#O(n+m)|O(n+m)
def merge_lists(lst1,lst2):
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []
    for i in range(len(lst1)+len(lst2)):
        result.append(i)
    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if (lst1[index_arr1] < lst2[index_arr2]):
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1
    while (index_arr1 < len(lst1)):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while (index_arr2 < len(lst2)):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result


#O(n2) | O(m)
def merge_lists2(lst1,lst2):
    idx1=0
    idx2=0
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1]> lst2[idx2]:
            lst1.insert(idx1,lst2[idx2])
            idx1+=1
            idx2+=1
        else:
            idx1+=1

    if idx2 < len(lst2):
        lst1.extend(lst2[idx2:])
    return lst1

print(merge_lists2([4, 5, 6], [-2, -1, 0, 7]))
