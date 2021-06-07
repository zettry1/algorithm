class InorderIterator:
    def __init__(self,root):
        self.stk=[]
        self.populate_iterator(root)

    def populate_iterator(self,root):
        while root != None:
            self.stk.append(root)
            root = root.left

    def hasNext(self):
        if not self.stk:
            return False
        else:
            return True

    def getNext(self):
        if not self.stk:
            return None

        r_val = self.stk[-1]

        del self.stk[-1]

        temp = r_val.right

        self.populate_iterator(temp)

        return r_val

def inorder_using_iterator(root):
    iter = InorderIterator(root)

    mystr=""

    while iter.hasNext():
        ptr = iter.getNext()
        mystr += str(ptr.data)+ " "
    return mystr


arr = [25,125,200,300,75,50,12,35,60,75]
root = create_BST(arr)
print("Inorder Iterator = ", end = "")
print(inorder_using_iterator(root))