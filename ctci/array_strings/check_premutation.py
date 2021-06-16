from typing import Counter


def check_premutation_by_sort(s1,s2):
    if len(s1) != len(s2):
        return False

    s1,s2 = sorted(s1), sorted(s2)

    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True


def check_premutation_by_count(str1,str2):
    if len(str1)!=len(str2):
        return False
    counter = [0]*256
    for c in str1:
        counter[ord(c)]+=1
    for c in str2:
        if counter[ord(c)]==0:
            return False
        counter[ord(c)]-=1
    return True

def check_premutation_pythonic(str1,str2):
    if len(str1)!=len(str2):
        return False

    return Counter(str1) == Counter(str2)

print(check_premutation_by_count('dog','godmog'))