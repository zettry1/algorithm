#A list such that each index has a product of all the numbers in the list except the number stored at that index.

#O(n)|O(n)
def find_product(list):
    left = 1
    product = []
    for ele in list:
        product.append(left)
        left = left*ele

    right = 1
    for i in range(len(list)-1,-1,-1):
        product[i] = product[i]*right
        right = right * list[i]
        print(product[i],list[i])
    return product



print(find_product([1,2,3,4]))