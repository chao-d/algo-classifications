"""
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList
to the right by ‘k’ nodes.
"""


def rotate(head, k):
    if not head or not head.next or k == 0:
        return head

    dummy = Node(0)
    dummy.next = head
    slow, fast = dummy, dummy
    n = k
    while n > 0 and fast.next:
        n -= 1
        fast = fast.next

    if fast.next is None:
        if n == 0:
            return head
        else:
            k = k % (k - n)
            return rotate(head, k)
    else:
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
