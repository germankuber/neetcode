# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        top_to_iterate = [root]
        
        solution = []
        while True:
            
            tmp_child = []
            solution_to_add = []
            some_item = False
            for node in top_to_iterate:
                solution_to_add.append(node.val)
                if node.left is not None:
                    tmp_child.append(node.left)
                    some_item = True
                if node.right is not None:
                    tmp_child.append(node.right)
                    some_item = True
            solution.append(solution_to_add)
            if some_item:
                
                top_to_iterate = tmp_child
            else: 
                break
            
        return solution