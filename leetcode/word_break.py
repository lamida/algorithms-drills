# https://leetcode.com/problems/word-break
from typing import Set, List

class Solution:
    def wordBreak(self, s: str, wordDict: Set[str]) -> bool:
        # we can alternatively use @lru_cache in python
        def wb(s: str, wordDict: Set[str], start: int, memo: List[bool]) -> bool:
            if len(s) == start:
                return True
            if memo[start]:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and wb(s, wordDict, end, memo):
                    memo[start] = True
                    return memo[start]
            memo[start] = False
            return memo[start]
        return wb(s, wordDict, 0, [False] * len(s))

if __name__ == "__main__":
    s = Solution()
    assert s.wordBreak("leetcode", {"leet", "code"}) == True
    assert s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]) == True
    assert s.wordBreak( s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]) == False
