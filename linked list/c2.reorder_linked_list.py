# Given the head of a Singly LinkedList, write a method to modify the
# LinkedList such that the nodes from the second half of the LinkedList are
# inserted alternately to the nodes from the first half in reverse order. So
# if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method
# should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList
# should be modified in-place.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.val) + " ", end='')
        temp = temp.next
        print()


def reorder(head):
    if head is None or head.next is None:
        return

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    sec_head = slow.next
    slow.next = None

    sec_head = reverse_list(sec_head)
    merge_lists(head, sec_head)
    return head


def reverse_list(head):
    if head is None or head.next is None:
        return head

    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def merge_lists(l0, l1):
    curr0, curr1 = l0, l1
    while curr0 and curr1:
        next0, next1 = curr0.next, curr1.next
        curr0.next = curr1
        curr1.next = next0
        curr0 = next0
        curr1 = next1
