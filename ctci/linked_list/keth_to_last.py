
def kth_to_last(ll,k):
    runner=current = ll

    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next
    return current