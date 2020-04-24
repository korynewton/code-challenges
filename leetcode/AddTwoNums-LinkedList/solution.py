# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = self.deconstruct_ll(l1)
        node2 = self.deconstruct_ll(l2)

        return self.output_result(node1 + node2)

    def deconstruct_ll(self, root):
        digits = []

        while root:
            digits.append(str(root.val))
            root = root.next

        digits.reverse()

        return int(''.join(digits))

    def output_result(self, num):
        if not num:
            return ListNode(0)

        digits = []

        while num > 0:
            digit = num % 10
            num = (num - digit) // 10
            digits.append(digit)

        root = ListNode(digits[0])
        stored_root = root
        for i in range(1, len(digits)):
            current = ListNode(digits[i])
            root.next = current
            root = current

        return stored_root
