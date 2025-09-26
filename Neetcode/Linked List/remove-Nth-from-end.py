# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        len = 0
        getLen = node = head
        while getLen:
            len += 1
            getLen = getLen.next 

        n = len - n
        while node and n > 1:
            node = node.next
            n -= 1
        
        if node == head and n == 0:
            head = node.next
        else:
            node.next = node.next.next

        return head
