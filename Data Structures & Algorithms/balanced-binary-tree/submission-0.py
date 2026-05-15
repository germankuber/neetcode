# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def navigate_depth(root: Optional[TreeNode])-> tuple[int, bool]:
            if not root:
                return 0, True
            
            left_depth, left_balanced = navigate_depth(root.left)
            right_depth, right_balanced = navigate_depth(root.right)
            
            if not left_balanced or not  right_balanced or abs(left_depth - right_depth) > 1:
                return 0, False
            
            return max(left_depth, right_depth) + 1, True
            
        
        _, balanced = navigate_depth(root)
        
        return balanced