# Recursive solution
#O(n) number of nodes | O(d) depth of tree
def invertBinaryTree(tree):
    if tree is None:
        return

    swapLeftandRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapLeftandRight(tree):
    tree.left , tree.right = tree.right ,tree.left



# Queue solution
#O(n) number of nodes | O(n)
def invertBinaryTree2(tree):
    queue = [tree]

    while len(queue):
        currentTree = queue.pop(0)
        if currentTree is None:
            continue
        swapLeftandRight(currentTree)
        queue.append(currentTree.left)
        queue.append(currentTree.right)





def swapLeftandRight(tree):
    tree.left , tree.right = tree.right ,tree.left
