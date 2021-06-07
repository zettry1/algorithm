class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def insert(root,key):
    if root is None:
        return Node(key)

    else:
        if root.data ==key:
            return root
        elif root.data < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if (root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if (root):
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if (root):
        postorder(root.left)
        postorder(root.right)
        print(root.data)

# Driver program to test the above functions
# Let us create the following BST
#       50
#    /     \
#   30      70
#  / \      / \
# 20  40    60  80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
preorder(r)