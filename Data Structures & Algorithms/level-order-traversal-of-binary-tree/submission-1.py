class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        top_to_iterate = [root]
        solution = []
        
        while True:
            tmp_child = []
            solution_to_add = []
            
            for node in top_to_iterate:
                solution_to_add.append(node.val)
                if node.left is not None:
                    tmp_child.append(node.left)
                if node.right is not None:
                    tmp_child.append(node.right)
            
            solution.append(solution_to_add)
            
            if not tmp_child:
                break
            top_to_iterate = tmp_child
        
        return solution