def findemiddle(lst):
    if lst.isEmpty():
        return -1

    currentNode = lst.get_head()

    if currentNode.next_element ==None:
        return currentNode.data

    mid_node = currentNode
    currentNode = currentNode.next_element

    while currentNode:
        mid_node= mid_node.next_element
        currentNode = currentNode.next_element
        if currentNode:
            currentNode= currentNode.next_element

    if mid_node:
        return mid_node.data
    return  -1
