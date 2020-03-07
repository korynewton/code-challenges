# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        lastNode = head
        length = 1
        while lastNode.next:
            lastNode = lastNode.next
            length += 1
        
        # attach head to last node making it a circular LL
        lastNode.next = head
        
        # get position of node that will be new end
        start_position = k % length
        
        # iterate through LL to get to node that will be the new end
        temp_head = head
        for _ in range(length - start_position -1):
            temp_head = temp_head.next
        
        # temp_head's next node will be the new root node
        root = temp_head.next
        #set temp_head next to None cuting off the end from what was a circular LL
        temp_head.next = None
        
        return root
        
