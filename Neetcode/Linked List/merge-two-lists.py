# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            # TODO change this?
            return None
        
        node = None
        while list1 or list2:
            if list1 and not list2:
                newVal = list1.val
                list1 = list1.next
            elif list2 and not list1:
                newVal = list2.val
                list2 = list2.next
            elif list1.val < list2.val:
                newVal = list1.val
                list1 = list1.next
            else:
                newVal = list2.val
                list2 = list2.next
                
                
            prev = node
            node = ListNode(newVal)
            if prev:
                prev.next = node
            else:
                head = node

        return head
        
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