
class LinkedList:
    def __init__(self,value):
        self.value=value
        self.next=None
#O(n)|O(1)
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode = nextDistinctNode
        currentNode.next = nextDistinctNode
    return linkedList

# removeDuplicatesFromLinkedList([123123])