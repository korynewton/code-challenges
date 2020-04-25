# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev_head = None
        pointer = head

        while pointer:
            # store next node
            next_node = pointer.next

            # set next of current pointer to rev_head
            pointer.next = rev_head
            # set new rev_head to pointer
            rev_head = pointer

            # move pointer forward
            pointer = next_node

        return rev_head
