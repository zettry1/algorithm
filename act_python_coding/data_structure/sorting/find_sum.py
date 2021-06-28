
def find_sum(lst,n):
    #nlog(n)
    lst.sort()

    left_idx=0
    right_idx=len(lst)-1

    while left_idx<right_idx:
        print(left_idx,right_idx)
        curr_sum = lst[left_idx]+lst[right_idx]

        if curr_sum < n:
            left_idx+=1
        elif curr_sum > n:
            right_idx-=1
        else:
            return [lst[left_idx],lst[right_idx]]

    return []

def find_sum_hash(lst,n):

    found_values=set()
    for ele in lst:
        if n-ele in found_values:
            return [n-ele,ele]
        found_values.add(ele)
lst = [1, 21, 3, 14, 5, 60, 7, 6]
n = 81

print(find_sum(lst,n))