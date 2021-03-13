# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        soln = []
        if len(s) == 0 or len(p) == 0 or len(s) < len(p): return soln
        
        
        dd = [0 for _ in range(26)]
        for c in p:
            dd[ord(c) - ord('a')]+= 1
            
        start = 0
        end = 0
        ln = len(p)
        diff = ln
        cur = ""
        for end in range(len(s)):
            if (end - start >= ln):
                cur = ord(s[start])
                dd[cur-ord('a')] += 1
                if dd[cur-ord('a')] > 0:
                    diff += 1
                start += 1
            cur = ord(s[end])
            dd[cur-ord('a')] -= 1
            if dd[cur-ord('a')] >= 0:
                diff -= 1
            if diff == 0:
                soln.append(start)
        return soln

    # less complex. Find the time complexity
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) == 0 or len(p) == 0 or len(s) < len(p): return []
        soln = []
        p = sorted(p)
        start = 0
        for end in range(len(p), len(s) + 1):
            start = end - len(p)
            if sorted(s[start:end]) == p:
                soln.append(start)
        return soln