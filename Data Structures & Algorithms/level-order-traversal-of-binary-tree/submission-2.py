from collections import deque
from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        
        result = []
        
        queue = deque([root])
        
        while queue:
            current_iteration = []
            for _ in range(len(queue)):
                item = queue.popleft()
                
                current_iteration.append(item.val)
                
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            
            result.append(current_iteration)
        return result
        