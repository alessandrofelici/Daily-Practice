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
        
        visited = set()

        def bfs(node: Optional['Node']):
            copy = Node(node.val)
            q = collections.deque()

            for v in node.neighbors:
                if v not in visited:
                    visited.add(v)
                    q.append(v)

            while q:
                neighbor = bfs(q.popleft())
                copy.neighbors.append(neighbor)
                neighbor.neighbors.append(copy)
            
            return copy

        visited.add(node)

        return bfs(node)