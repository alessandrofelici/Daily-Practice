from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
          root.left = self.insertIntoBST(root.left, val)
        else:
          root.right = self.insertIntoBST(root.right, val)

        return root

sol = Solution()
node1 = TreeNode(1, None, None)
node4 = TreeNode(4, None, None)
node9 = TreeNode(9, None, None)
node3 = TreeNode(3, node1, node4)
node5 = TreeNode(5, node3, node9)

print(sol.insertIntoBST(node5, 6).val)