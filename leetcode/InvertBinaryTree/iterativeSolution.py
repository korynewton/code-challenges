# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        else:
            #utilize a queue to swap out left and right child of all nodes 
            #as we iterate through the tree
            queue = []
            queue.append(root)
            while len(queue) > 0:
                current = queue.pop()
                
                #store one child in temporary variable
                temporary = current.right
                current.right = current.left
                current.left = temporary
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return root