# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
          self.callback(root, 0)
        return self.balanced

        

    def callback(self, root: Optional[TreeNode], height) -> int:
        if root is None:
            return height - 1
        
        left, right = self.callback(root.left, height + 1), self.callback(root.right, height + 1)

        if abs(left - right) > 1:
            self.balanced = False
        
        return max(left, right)