from typing import List

class Node:
    def __init__(self, data: int, next: "Node" = None):
        self.data = data 
        self.next = next

# This solution is bloated :(
def reverse(head: Node) -> Node:
    # add surrogate prefix for easier handling
    if head and head.data % 2 == 0:
        head = Node(-1, head)
    outer = head
    while outer:
        current = outer
        prev = None

        # find start even
        while current and current.data % 2 != 0:
            prev = current
            current = current.next
        startEven = current
        # find end even
        while current and current.data % 2 == 0:
            current = current.next
        endEven = current

        rrev = rev(startEven, endEven)
        # connect from the head
        if prev:
            prev.next = rrev
        outer = endEven
    return head if head.data != -1 else head.next

"""
Really bloated
"""
def rev(head: Node, tail: Node) -> Node:
    current = head
    prev = None
    next = None
    while current and current.data % 2 == 0:
        next = current.next
        current.next = prev
        prev = current
        current = next
    rev = prev
    current = rev
    # attach the tail
    while current:
        prev = current
        current = current.next
    prev.next = tail
    return rev

if __name__ == "__main__":
    # l = Node(1, Node(2, Node(8, Node(9, Node(12, Node(16))))))
    # x = reverse(l)

    # current = x
    # while current:
    #     print(current.data)
    #     current = current.next

    print("####")

    l = Node(2, Node(18, Node(24, Node(3, Node(5, Node(7, Node(9, Node(6, Node(12)))))))))
    x = reverse(l)

    current = x
    while current:
        print(current.data)
        current = current.next