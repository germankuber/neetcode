class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        top_to_iterate = [root]
        solution = []
        
        while True:
            tmp_child = []
            last_val = None
            
            for node in top_to_iterate:
                last_val = node.val
                if node.left is not None:
                    tmp_child.append(node.left)
                if node.right is not None:
                    tmp_child.append(node.right)
            
            solution.append(last_val)
            
            if not tmp_child:
                break
            top_to_iterate = tmp_child
        
        return solution