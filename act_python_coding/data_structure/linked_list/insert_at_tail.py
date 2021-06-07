from .link.myLinkedList import LinkedList
from .link.myNode import Node


def insert_at_tail(lst, value):
    # Creating a new node
    new_node = Node(value)

    # Check if the list is empty, if it is simply point head to new node
    if lst.get_head() is None:
        lst.head_node = new_node
        return

    # if list not empty, traverse the list to the last node
    temp = lst.get_head()

    while temp.next_element:
        temp = temp.next_element

    # Set the nextElement of the previous node to new node
    temp.next_element = new_node
    return

lst = LinkedList()
lst.print_list()
insert_at_tail(lst, 0)
lst.print_list()
insert_at_tail(lst, 1)
lst.print_list()
insert_at_tail(lst, 2)
lst.print_list()
insert_at_tail(lst, 3)
lst.print_list()
