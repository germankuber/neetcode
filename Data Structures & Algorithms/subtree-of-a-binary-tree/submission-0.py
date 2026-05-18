# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def iterate_internal_tree(root: Optional[TreeNode], subRoot: Optional[TreeNode])-> bool:
            if root is None and subRoot is None:
                return True
            
            if root is None and subRoot:
                return False
            
            if root and subRoot is None:
                return False
            
            if root.val != subRoot.val:
                return False
            
            left_result = iterate_internal_tree(root.left, subRoot.left)
            
            right_result = iterate_internal_tree(root.right, subRoot.right)
            
            return left_result and right_result
        
        def iterate_tree(root : Optional[TreeNode]) -> bool:
            
            if root is None:
                return False
            
            if root.val == subRoot.val:
                result = iterate_internal_tree(root, subRoot)
                if result:
                    return result
            
            result_left = iterate_tree(root.left)
            
            result_right = iterate_tree(root.right)
            
            return result_left or result_right
        
        return iterate_tree(root)