# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def depth_first_path(self, root, x):
        # Returns a path list from root to x
        
        visited = set()
        stack = []
        stack.append([root])
        
        while stack:
            path = stack.pop()
            current = path[-1]
            
            if current not in visited:
                if current == x:
                    return path
                visited.add(current)
            
            if current.left:
                left_path = list(path)
                left_path.append(current.left)
                stack.append(left_path)
            if current.right:
                right_path = list(path)
                right_path.append(current.right)
                stack.append(right_path)

                
        # If node not found then doesnt exist
        return False
                
                
            
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Retrieve a depth firt path from root to node for p and q
        p_path = self.depth_first_path(root,p)
        q_path = self.depth_first_path(root,q)
        
        
        # Iterate backwards through p_path and return the first node
        # that is also for in q_path
        for i in range(len(p_path)-1,-1,-1):
            if p_path[i] in q_path:
                return p_path[i]
        
      
            
       
        

        
