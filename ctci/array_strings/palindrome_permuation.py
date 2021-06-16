from collections import Counter


def is_palindrome_permutation(phrase):
    table =[0 for _ in range(ord('z'-ord('a')+1))]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x!=-1:
            table[x]+=1
            if table[x] %2:
                countodd+=1
            else:
                countodd-=1
    return countodd<=1


def char_number(c):
    a = ord("a")
    z = ord("z")

    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c)

    if a <= val <=z:
        return val - a

    if upper_a <= a <=upper_z:
        return val - upper_a
    return -1


def is_palindrom_permuation_pythonic(phrase):
    counter = Counter(phrase.replace(" ","").lower())
    print('counter',counter)
    for val in counter.values():
        print(val, val%2)
    return sum(val%2 for val in counter.values())<=1


print(is_palindrom_permuation_pythonic("aaacccaaa"))