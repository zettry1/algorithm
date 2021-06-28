
def bubble_sort(arr):


    for i in range(len(arr)):

        for j in range(0,len(arr)-i-1):
            print('len(arr)-i-1',len(arr)-i-1)
            # print(arr[j])
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(arr)



if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4,6,1,0]
    bubble_sort(lst)  # Calling bubble sort function

    print("Sorted list is: ", lst)
