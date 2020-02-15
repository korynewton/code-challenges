def subtreeWithAllDeepest(self, root):
    # annotated each nodes depth in relation to parent
    depth_annotated = {None: -1}
    def depth_first_search(node, parent = None):
        if node:
            depth_annotated[node] = depth_annotated[parent] + 1
            depth_first_search(node.left, node)
            depth_first_search(node.right, node)
    depth_first_search(root)

    max_depth = max(depth_annotated.values())

    def max_depth_subtree(node):
        if not node or depth_annotated.get(node, None) == max_depth:
            return node
        left_child, right_child = max_depth_subtree(node.left), max_depth_subtree(node.right)
        
        if left_child and right_child:
            #if left and right child equal max depth then,
            #the answer is the parent
            return node
        elif left_child:
            #if only one child is equal to the max depth return
            return left_child
        else:
            return right_child

    return max_depth_subtree(root)
  



        
