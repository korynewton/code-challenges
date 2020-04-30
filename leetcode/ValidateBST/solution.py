# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateTree(root)

    def validateTree(self, node: TreeNode, lower_limit=float('-inf'), upper_limit=float('inf')):
        if not node:
            return True

        val = node.val
        # check if nodes value violates upper or lower limits
        if val <= lower_limit or val >= upper_limit:
            return False

        # call validateTree again adjusting lower and upper limits as necessary for the branch
        if not self.validateTree(node.right, val, upper_limit):
            return False
        if not self.validateTree(node.left, lower_limit, val):
            return False
        return True

