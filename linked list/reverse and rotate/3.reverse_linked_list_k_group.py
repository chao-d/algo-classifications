"""
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized
sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements,
reverse it too.
"""


def reverse_every_k_elements(head, k):
    if not head or not head.next or k < 2:
        return head

    dummy = Node(0)
    dummy.next = head
    slow, fast = dummy, dummy
    n = k
    while fast:
        if n > 0:
            fast = fast.next
            n -= 1
        else:
            tail = fast.next
            fast.next = None
            prev, curr = tail, slow.next
            next_pos = slow.next
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            slow.next = prev
            slow, fast = next_pos, next_pos
            n = k

    return dummy.next
