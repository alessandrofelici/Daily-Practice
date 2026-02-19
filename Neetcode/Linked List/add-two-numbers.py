from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        head = None
        prev = None

        while l1 and l2:
            sum = l1.val + l2.val + carry 
            
            carry = sum//10
            sum %= 10
            
            if head:
                prev.next = ListNode(val=sum)
                prev = prev.next
            else:
                head = ListNode(val=sum)
                prev = head
            
            l1 = l1.next
            l2 = l2.next

        while l1 or l2:
            sum = l1.val if l1 else l2.val
            sum += carry

            carry = sum//10
            sum %= 10

            prev.next = ListNode(val=sum)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            prev.next = ListNode(1)

        return head