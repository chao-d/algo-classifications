"""
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function
to return the new head of the reversed LinkedList.
"""


def reverse(head):
    if not head or not head.next:
        return head

    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
