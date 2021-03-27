# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
if both l1 and l2 are not empty, compare the value and append lowest to the result.

Last iterate the remaining of l1 or l2 and append to result.
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        result = head
        while l1 and l2:
            if l1.val < l2.val:
                result.next = l1
                result = result.next
                l1 = l1.next
            else:
                result.next = l2
                result = result.next
                l2 = l2.next
                
        result.next = l1 if l1 else l2

        """
        Instead of iterate the remaining LinkedList element, just attach the tail of result to the
        remained list. See above.
        """
        # while l1:
        #     result.next = l1
        #     result = result.next
        #     l1 = l1.next
        
        # while l2:
        #     result.next = l2
        #     result = result.next
        #     l2 = l2.next
            
        return head.next