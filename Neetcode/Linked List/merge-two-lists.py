# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
        
        # index i j
        # while ()
        #   find lesser val
        #   append it to new list
        #   inc val of list taken from
        #   case i: [j] > [i]
        #     append[j], ++j
        #   case ii: else
        #     append[i], ++i

        # since l.l., do this instead of append
        # node = ListNode(list1.head.value, )