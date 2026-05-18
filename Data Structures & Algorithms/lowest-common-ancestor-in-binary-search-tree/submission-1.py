class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return
        if root.val == p.val:
            return p

        if root.val == q.val:
            return q
        if p.val < root.val < q.val:
            return root
        
        if p.val > root.val > q.val:
            return root

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        else:
            return self.lowestCommonAncestor(root.left, p, q)