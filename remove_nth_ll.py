# Hasn't handle this case well
# l = ListNode(1, ListNode(2, ListNode(3, ListNode(10, ListNode(100)))))
# s.removeNthFromEnd(l, 4)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        i = 0
        while i < n + 1 and cur is not None:
            cur = cur.next    
            i+=1
        
        ret = head
        follow = ret
        while cur is not None:
            cur = cur.next
            follow = follow.next
            
        next = None if follow.next is None else follow.next.next
        follow.next = next
        return ret

if __name__ == "__main__":
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(10, ListNode(100)))))
    # l = ListNode(1)
    s.removeNthFromEnd(l, 4)
    c = l
    while c is not None:
        print(c.val)
        c = c.next
