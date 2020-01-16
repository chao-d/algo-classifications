"""
Given the head of a LinkedList and a number ‘k’, reverse every alternating
‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements,
reverse it too.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_alternate_k_elements(head, k):
    if not head or not head.next or k < 2:
        return head

    dummy = Node(0)
    dummy.next = head
    slow, fast = dummy, dummy
    n = k
    reverse_group = True
    while fast:
        if not reverse_group:
            if n > 0 and fast.next:
                fast = fast.next
                slow = slow.next
                n -= 1
            else:
                reverse_group = not reverse_group
                n = k
        else:
            if n > 0 and fast.next:
                fast = fast.next
                n -= 1
                continue
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
            reverse_group = not reverse_group

    return dummy.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
