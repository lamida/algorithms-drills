# https://leetcode.com/problems/valid-palindrome-ii
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palin(s: str, left: int, right: int) -> bool:
            while left < right:
                if s[left]!=s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if is_palin(s, left, right - 1):
                    return True
                if is_palin(s, left + 1, right):
                    return True
                return False
        return True