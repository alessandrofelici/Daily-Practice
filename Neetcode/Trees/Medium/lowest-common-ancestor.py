# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root.val == p.val or root.val == q.val:
            return root
        if root.val < min(p.val, q.val) and root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > max(p.val, q.val)  and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root