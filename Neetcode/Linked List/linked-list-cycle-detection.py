# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = ptr2 = head
        while ptr1.next != None:
            ptr1 = ptr1.next
            if ptr2 != None and ptr2.next != None:
                ptr2 = ptr2.next.next
            else:
                return False
            if ptr1 == ptr2:
                return True
        
        return False