from typing import List
from collections import deque

"""
There are only to fundamentals data structures. First is Array and second is LinkedList.

Let's talk about LinkedList now.
"""

class ListNode:
    def __init__(self, val: int, next: "ListNode" = None):
        self.val = val
        self.next = next

def listToLinkedList(list: List[int]) -> ListNode:
    def append(node: ListNode, nextVal: int) -> ListNode:
        node.next = ListNode(nextVal)
        return node.next
    list = deque(list)
    head = ListNode(list.popleft())
    current = head
    while list:
        current = append(current, list.popleft())
    return head

def printLinkedList(head: ListNode):
    current = head
    while current:
        print(current.val)
        current = current.next

"""
Preorder LinkedList Traversal
"""

def preorder(head: ListNode):
    if head:
        # do something first on the current node
        print(head.val)
        # then process the rest
        preorder(head.next)

"""
Postorder LinkedList Traversal
"""

def postorder(head: ListNode):
    if head:
        # traverse next first till the end
        postorder(head.next)
        # then only process the current node
        print(head.val)

if __name__ == "__main__":
    ll = listToLinkedList(list(range(10)))
    # printLinkedList(ll)

    preorder(ll)
    postorder(ll)





        