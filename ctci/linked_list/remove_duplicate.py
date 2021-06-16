def remove_duplicate(head):
    if head.next is None:
        return head
    current = head
    while current and current.next :
        if current.data  == current.next.data:
            current.next = current.next.next
        current = current.next

    return current


def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll

def remove_dups_followup(ll):
    runner = current = ll.head

    while current:
        runner= current
        while runner.next:
            if runner.next.value == current.value:
                runner.next  = runner.next.next
            else:
                runner = runner.next
            runner = current.next
    ll.tail = runner
    return ll