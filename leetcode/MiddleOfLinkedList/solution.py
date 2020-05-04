# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #inititalize a fast and slow pointer
        fast = slow = head
        
        #while we are not at the end and not at last node, keep incrementing pointers
        while fast and fast.next != None:
            #increment fast twice as fast as slow
            fast = fast.next.next
            slow = slow.next
            
        #when fast reaches the end slow should be at middle node
        return slow
        
