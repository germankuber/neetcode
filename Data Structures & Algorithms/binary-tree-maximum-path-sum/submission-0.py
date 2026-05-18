# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = []
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            res = 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(left, 0) + max(right, 0) + root.val
            
            self.result.append(res)

            return root.val + max(max(right, left), 0)

        self.result.append(dfs(root))

        return max(self.result)