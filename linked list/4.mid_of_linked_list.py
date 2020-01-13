# Given the head of a Singly LinkedList, write a method to return the middle
# node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second
# middle node.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow.next
