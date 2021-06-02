#O(n*k)
def max_sub_array_of_size_k_2(k,arr):
    max_sum,window_sum=0,0
    for i in range(len(arr)-k+1):
        window_sum=0
        for j in range(i,i+k):
            window_sum+=arr[j]
        max_sum=max(max_sum,window_sum)
    return max_sum


#O(n)
def max_sub_array_of_size_k(k, arr):
  max_sum , window_sum = 0, 0
  window_start = 0
  for window_end in range(len(arr)):
    print('window_end',window_end)
    window_sum += arr[window_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead
  return max_sum



print(max_sub_array_of_size_k_2(3, [2, 1, 5, 1,4, 3, 2]))