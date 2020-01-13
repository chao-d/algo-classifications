# Given the head of a Singly LinkedList, write a function to determine if the
# LinkedList has a cycle in it or not.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
