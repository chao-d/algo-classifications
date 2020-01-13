# Given the head of a Singly LinkedList that contains a cycle, write a function
# to find the starting node of the cycle.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def find_cycle_start(head):
    fast, has_cycle = hasCycle(head)
    if not has_cycle:
        return fast
    fast = fast.next
    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return fast


def hasCycle(head):
    if head is None or head.next is None:
        return None, False

    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow, True
    return None, False
