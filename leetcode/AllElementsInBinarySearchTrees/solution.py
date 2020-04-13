# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def traverse_tree(self, root):
        tree_vals = []

        if root:
            to_traverse = []
            to_traverse.append(root)
            while to_traverse:
                current = to_traverse.pop()
                tree_vals.append(current.val)
                if current.left:
                    to_traverse.append(current.left)
                if current.right:
                    to_traverse.append(current.right)

            return tree_vals

        else:
            return tree_vals

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        root1_elements = self.traverse_tree(root1)
        root2_elements = self.traverse_tree(root2)

        all_elements = root1_elements + root2_elements
        all_elements.sort()

        return all_elements
