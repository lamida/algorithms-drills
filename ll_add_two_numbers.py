
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.add(l1, l2, 0)

    def add(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        if l1 is None and l2 is None and carry == 0:
            return None

        total = carry
        if l1 is not None:
            total += l1.val

        if l2 is not None:
            total += l2.val

        result = ListNode(total % 10)

        if l1 is not None or l2 is not None:
            l1Next = l1.next if l1 is not None else None
            l2Next = l2.next if l2 is not None else None
            nextCarry = 1 if total >= 10 else 0
            result.next = self.add(l1Next, l2Next, nextCarry)
        return result


if __name__ == "__main__":
    print("result is")
    sol = Solution()
    # 7 -> 0 -> 8
    res = sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))),
                            ListNode(5, ListNode(6, ListNode(4))))
    while res is not None:
        print(res.val)
        res = res.next
