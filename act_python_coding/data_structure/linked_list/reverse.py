def reverse(lst):
  previous = None
  next = None
  current = lst.get_head()

  while current:
    next = current.next_element
    current.next_element = previous
    previous = current
    current = next

    lst.head_node = previous
  return lst