# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    First approach is just convert LinkedList to array and do palindrome checking to array.
    """
    def isArrayPalindrome(self, arr: List[int]) -> bool:
        l = 0
        r = len(arr)-1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l+=1
            r-=1
        return True
    
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.isArrayPalindrome(arr)
        