def is_subset(list1, list2):
    s = set(list1)  # Create a set with list1 values
    print(s)
    # Traverse list 2 elements
    for elem in list2:
        # Return false if an element not in list1
        if elem not in s:
            return False
    # Return True if all elements in list1
    return True


list1 = [9, 4, 7, 1, -2, 6, 5]
list2 = [7, 1, -2]
list3 = [10, 12]
print(is_subset(list1, list2))
print(is_subset(list1, list3))
