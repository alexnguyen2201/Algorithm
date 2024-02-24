def fn(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def fn(head):
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev
