# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        visible = []

        def dfs(root: Optional[TreeNode], depth: int):
            if not root:
                return
            
            if len(visible) == depth:
                visible.append(root.val)
            
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        
        return visible
    

# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
#         visible, levels = [], []

#         def dfs(root: Optional[TreeNode], level: int):
#             if not root:
#                 return
            
#             if len(levels) <= level:
#                 levels.append([])
            
#             levels[level].append(root.val)
#             dfs(root.left, level + 1)
#             dfs(root.right, level + 1)

#         dfs(root, 0)

#         for i in range(len(levels)):
#             visible.append(levels[i][len(levels[i]) - 1])
        
#         return visible