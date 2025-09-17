# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # count list len
        next_node = head.next
        length = 1
        while next_node is not None:
            length += 1
            next_node = next_node.next
        
        # also get half point
        mid_node = head.next
        for i in range(length/2):
            mid_node = next_node.next
        mid_node = self.reverseList(mid_node)
        
        # split list (1, n/2) & (n/2 + 1, n-1)
        first_node = head.next
        for i in range(length):
            new1 = ListNode(mid_node.val, first_node)
            if mid_node.next:
              new2 = ListNode(first_node.val, mid_node.next)
            else:
              new2 = ListNode(first_node.val, None)

        # reverse l2

        # while
        # l2 append
        # l1 append

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev, curr, nextNode = None, head, head.next
        while nextNode != None:
            curr.next = prev
            prev = curr
            curr = nextNode
            if curr != None:
              nextNode = curr.next
        curr.next = prev
        return curr