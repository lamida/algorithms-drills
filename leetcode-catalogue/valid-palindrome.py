# Iterate from left and right. Lowercase left and right. Skip for non alphanum characters.
# 
# Stop if there is a mismatch and return False.
#
# Last, return True.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            left = s[l].lower()
            right = s[r].lower()
            if not left.isalnum():
                l += 1
                continue
            if not right.isalnum():
                r -= 1
                continue
            if left != right:
                return False
            l += 1
            l -= 1
        return True
