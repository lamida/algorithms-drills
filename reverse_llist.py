
class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next
    

"""
1 -> 2 -> 3 -> 4 -> None
None <- 1 <- 2 <- 3 <- 4
"""
def reverse(head: ListNode) -> ListNode:
    current = head # walker
    next = None # point to the next element
    prev = None # point to the prev element
    while current is not None:
        next = current.next # Save pointer to next
        current.next = prev # make next pointer to prev. swap the arrow from facing front to facing back
        prev = current # current becomes prev 
        current = next # move pointer forward
    return prev # in the last iteration we just care the last current which is referred by prev

def llprint(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print("Original")
    llprint(ll)
    rev = reverse(ll)
    print("Reversed")
    llprint(rev)

