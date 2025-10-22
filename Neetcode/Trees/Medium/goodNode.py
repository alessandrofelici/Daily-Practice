# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, prev: int):
            if root is None:
                return
            
            if root.val >= prev:
                self.count += 1
            
            dfs(root.left, max(root.val, prev))
            dfs(root.right, max(root.val, prev))
        
        self.count = 0
        dfs(root, root.val)

        return self.count
        