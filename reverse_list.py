# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/2378/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pass
        
if __name__ == "__main__":
    sol = Solution()
    l = sol.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    while l is not None:
        print(l.val)
        l = l.next
    
