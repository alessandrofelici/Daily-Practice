from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        copied = {}

        def dfs(node: Optional['Node']):
            copied[node] = Node(node.val)

            for v in node.neighbors:
                if v not in copied:
                    copied[v] = dfs(v)
                copied[node].neighbors.append(copied[v])
            
            return copied[node]

        return dfs(node)