from stack import MyStack
def next_greater_element(lst):
    stack = MyStack()
    res = [-1]*len(lst)

    for i in range(len(lst)-1,-1,-1):
        while not stack.is_empty() and stack.peek()<= lst[i]:
            stack.pop()
        if not stack.is_empty():
            print(stack.peek())
            res[i]= stack.peek()

        stack.push(lst[i])
    print(res)



next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9])