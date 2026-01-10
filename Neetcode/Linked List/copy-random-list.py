
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

class Solution:
    nodes = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node = Node(head.val)
        self.nodes[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.nodes[head.random] if head.random else None

        return node