from typing import List

"""
We will recurse based on the idx. The base case will be when idx which is equivalent
with the stack dept reaches the size of len(s). In each of non base case, we will swap
element between idx and len(s) - 1. See permutation1.png for the ilustration.
"""
def permutation(s: List[str]) -> List[List[str]]:
    results = []
    def backtrack(candidate: List[str], idx: int = 0):
        if idx == len(s) - 1: # the base case is when the depth of recursion equal to len(s) - 1
            results.append(candidate[:])
        else:
            for i in range(idx, len(s)): # must start the iteration from idx!
                candidate[idx], candidate[i] = candidate[i], candidate[idx]
                backtrack(candidate, idx + 1)
                candidate[idx], candidate[i] = candidate[i], candidate[idx]
    backtrack(s)
    return results

"""
We will recurse based on the depth. The base case will be when the resulted
candidate is at the same size as original string. In each of non base case,
we will get what is current character of the current stack, then will insert 
the current character in all the index for the next stack. See permutation2.png
for the ilustration.
"""
def permutation2(s: List[str]) -> List[List[str]]:
    results = []
    def backtrack(candidate: List[str], depth: int = 0): 
        if len(candidate) == len(s):
            results.append(candidate[:])
        else:
            current = s[depth]
            newCandidate = candidate[:]
            for i in range(depth + 1):
                newCandidate.insert(i, current)
                backtrack(newCandidate, depth + 1)
                newCandidate = candidate[:]
    backtrack([])
    return results

if __name__ == "__main__":
    print(permutation2([i for i in "ABC"]))
    print(permutation2([]))
