

#O(n)| time | O(d)
def productSum(array,multiplier=1):
    sum =0
    for element in array:
        if type(element) is list:
            sum+=productSum(element,multiplier+1)
        else:
            sum+=element
    return sum*multiplier


print(productSum([5,2,[7,-1],3,[6,[-13,8],4],5]))