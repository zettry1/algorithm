# Python program to print level
# order traversal using Queue
from collections import deque
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.val = key
        self.left = None
        self.right = None

# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)
    while(len(queue) > 0):
        # Print front of queue and
        # remove it from queue
        print (queue[0].val)
        node = queue.pop(0)

        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


def levelOrderTraversal(root):
    if not root:
        return []
    queue, res = deque([root]),[]

    while queue:
        cur_level , size = [] , len(queue)
        print('size',size)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            cur_level.append(node.val)

        res.append(cur_level)
    print(res)
    return res
#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level Order Traversal of binary tree is -")
levelOrderTraversal(root)