
def selection(arr):

    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            print(arr[j])
            if arr[min_index]>arr[j]:
                min_index=j

        arr[i],arr[min_index] = arr[min_index], arr[i]

# Driver code to test above
if __name__ == '__main__':

    arr = [3, 2, 1, 5, 4,5,6]
    selection(arr)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", arr)