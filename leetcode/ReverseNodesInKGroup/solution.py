# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        pointer = head
        k_tail = None

        new_head = None

        while pointer:
            count = 0

            stored_head = pointer

            # iterate through next k to see if there are k nodes left
            while pointer and count < k:
                pointer = pointer.next
                count += 1

            # if we havent reached the end of the LL, reverse the k section
            if count == k:
                reversed_k_head = self.revese_k_nodes(stored_head, k)

                # if new head has not been established, reversed_k_head is the new head
                if not new_head:
                    new_head = reversed_k_head

                # connect previous k_tail to reversed_k_head
                if k_tail:
                    k_tail.next = reversed_k_head

                # previous head is now the end of the reversed_list
                k_tail = head
                head = pointer

        if k_tail:
            k_tail.next = head

        return new_head if new_head else head

    def revese_k_nodes(self, head, k):
        # revese k nodes, return LL
        rev_head = None
        pointer = head

        while k:
            next_node = pointer.next

            pointer.next = rev_head
            rev_head = pointer

            pointer = next_node

            k -= 1

        return rev_head
