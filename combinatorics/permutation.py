from typing import List

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

if __name__ == "__main__":
    print(permutation([i for i in "ABC"]))
