# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def traverse(nodes, level_order_list):
            if not nodes:
                # if nothing left in nodes list, we have hit the end of the tree
                return level_order_list
            else:
                # build list of nodes that are connected to current level
                to_traverse = []
                # append values from this level
                level = []
                for node in nodes:
                    if not node:
                        continue

                    level.append(node.val)

                    if node.left:
                        to_traverse.append(node.left)
                    if node.right:
                        to_traverse.append(node.right)

                level_order_list.append(level)

                return traverse(to_traverse, level_order_list)

        return traverse([root], [])
