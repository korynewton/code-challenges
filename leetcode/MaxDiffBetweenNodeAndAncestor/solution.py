# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_diff = 0
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        #recursive dfs to store the max and min values seen in ancestral line
        def dfs(node, prev_max, prev_min):
            if not node:
                return
            else:
                current_max = max(prev_max, node.val)
                current_min = min(prev_min, node.val)
                self.max_diff = max(self.max_diff, current_max - current_min)
                dfs(node.left, current_max, current_min)
                dfs(node.right, current_max, current_min)
        
        dfs(root, float('-inf'), float('inf'))
        return self.max_diff
        
