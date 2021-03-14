# Old permutation attempt. See permutation.py for more thoughtful attempt.
from typing import List
def permutate(arr: List[int]) -> List[List[int]]:
    res = []

    if len(arr) == 0: return []
    if len(arr) == 1: return [arr]

    for i in range(len(arr)):
        current = arr[i]
        rems = arr[0:i] + arr[i+1:]
        perem = permutate(rems)

        for j in range(len(perem)):
            candidate = [current] + perem[j]
            res += [candidate]
    return res

if __name__ == "__main__":
    print(permutate([1,2,3]))
