"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the
LinkedList from position ‘p’ to ‘q’.
"""


def reverse_sub_list(head, m, n):
    dummy = Node(-1)
    dummy.next = head
    slow, fast = dummy, dummy
    diff = n - m
    if diff == 0:
        return head

    while diff > 0:
        fast = fast.next
        diff -= 1

    prev = dummy
    while m > 0:
        prev = slow
        slow = slow.next
        fast = fast.next
        m -= 1

    tail = fast.next
    fast.next = None

    p, curr = tail, slow
    while curr:
        next = curr.next
        curr.next = p
        p = curr
        curr = next

    prev.next = fast
    return dummy.next
