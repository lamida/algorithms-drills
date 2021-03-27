# We need a helper function that do a simple valindrome check.
# In the main function, we will check from left to center and right to center first,
# then in the case of mismatch, we will proceed 1 extra character to the right and also
# check to palindrome for one extra character to the left. If any of the check is ok, then 
# it means the character is still palindrome, after removing one of the char.
#
# space complexity is O(1) no additional memory. time complexity is O(2n) which is O(n).
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str, l: int, r: int) -> bool:
            while l < r:
                left = s[l]
                right = s[r]
                if left != right:
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            left = s[l]
            right = s[r]
            if left != right:
                if isPalindrome(s, l + 1, r):
                    return True
                if isPalindrome(s, l, r - 1):
                    return True
                return False
            l += 1
            r -= 1
        return True