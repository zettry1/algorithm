def anagrams(lst):

    dictionary={}

    for string in lst:

        key =''.join(sorted(string))

        if key in dictionary.keys():
            dictionary[key].append(string)

        else:
            dictionary[key] =[]
            dictionary[key].append(string)
    print(dictionary)

    result =[]

    for key , value in dictionary.items():
        if len(value) >=2:
            result.append(value)

    result = sorted(result)

    return result


if "__main__" == __name__:

    lst = ['tom marvolo riddle ', 'abc', 'def', 'cab', 'fed', 'clint eastwood ', 'i am lord voldemort', 'elvis', 'old west action', 'lives']
    print (anagrams(lst))
