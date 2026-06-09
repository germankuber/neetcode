from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def validate_sub_tree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return validate_sub_tree(root.left, subRoot.left) and validate_sub_tree(root.right, subRoot.right)
        
        def dfs(root : Optional[TreeNode])-> bool:
            if not root:
                return False
            
            
            if root.val == subRoot.val:
                if validate_sub_tree(root, subRoot):
                    return True
                
            return dfs(root.left) or dfs(root.right)   
        
        return dfs(root)
    
                
        
        