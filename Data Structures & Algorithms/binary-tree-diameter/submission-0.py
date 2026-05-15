# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            
            left_depth, longest_left = dfs(node.left)
            right_depth, longest_right = dfs(node.right)
            
            broad = left_depth + right_depth
            max_current_long = max(longest_left, longest_right, broad)
            
            return (max(left_depth, right_depth) + 1, max_current_long)
        
        _, diameter = dfs(root)
        return diameter