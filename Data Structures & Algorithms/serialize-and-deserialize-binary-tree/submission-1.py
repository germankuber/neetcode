# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        list_values = []
        def dfs(root: Optional[TreeNode]):
            
            if not root:
                list_values.append("*")
                return
            
            
            list_values.append(str(root.val))
            
            dfs(root.left)
            dfs(root.right)
            
        dfs(root=root)
        return ",".join(list_values)
        


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes =  iter(data.split(","))
        
        def build():
            val = next(nodes)
            if val == "*":
                return None
            else:
                return TreeNode(val=int(val), left=build(), right=build())
        
        return build()
        