# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_sum = ''
        l2_sum = ''
        
        #Loop through both LLs and concatenate string representation of nums
        while l1:
            l1_sum += str(l1.val)
            l1 = l1.next
        
        while l2:
            l2_sum += str(l2.val)
            l2 = l2.next
        
        #Convert nums to int, add and then convert back to string
        total_str = str(int(l1_sum) + int(l2_sum))
        
        #Loop through total creating LL, return root
        root = ListNode(total_str[0])
        current = root
        for i in range(1,len(total_str)):
            current.next = ListNode(total_str[i])
            current = current.next
        
        return root
