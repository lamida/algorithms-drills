# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
x    1->2->3->x
        nxt
     c
p
x<-1<-2<-3

The iterative solution requires 3 pointers:
current is the current element we are processing.
previous is to track the previous element.
nxt is the pointer to the current.next element.

We need to update the pointer in this order:
1. put current.next in nxt temporary holder
2. point current.next backward
3. update prev pointer to current, for the next cycle processing
4. point current to the right side of the next element
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev
    
    def reverseList_iter(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
        