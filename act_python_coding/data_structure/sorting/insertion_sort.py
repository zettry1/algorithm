def insertion_sort(arr):

    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key< arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key


# Driver code to test above
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    insertion_sort(lst)  # Calling insertion sort function

    print("Sorted list is: ", lst)