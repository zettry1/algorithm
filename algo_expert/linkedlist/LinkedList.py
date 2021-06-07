class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.value)
            printval = printval.next
    def test_case_1(self):
        test = SLinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = SLinkedList(1).addMany([3, 4, 5, 6])
        # actual = program.removeDuplicatesFromLinkedList(test)
        # self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())

list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")


# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3
e3.next = e4
list1.Atbegining('Fri')
list1.listprint()
