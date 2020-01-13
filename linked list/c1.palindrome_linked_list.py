# Given the head of a Singly LinkedList, write a method to check if the
# LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be
# in the original form once the algorithm is finished. The algorithm should
# have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def is_palindromic_linked_list(head):
    hhead = sec_head(head)
    if head == hhead:
        return True

    new_head = reverse_list(hhead)
    curr = head

    while curr and new_head:
        if curr.val != new_head.val:
            return False
        curr = curr.next
        new_head = new_head.next

    return True


def sec_head(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow.next


def reverse_list(head):
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
