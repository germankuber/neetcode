from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode], count: int) -> tuple[int, Optional[int]]:
            if not node:
                return count, None
            
            # izquierda primero (los más chicos)
            count, found = dfs(node.left, count)
            if found is not None:
                return count, found
            
            # visito el nodo actual
            count += 1
            if count == k:
                return count, node.val
            
            # derecha
            return dfs(node.right, count)
        
        _, result = dfs(root, 0)
        return result