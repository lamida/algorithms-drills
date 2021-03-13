from typing import List

def combination(s: List[str]) -> List[List[str]]:
    def combi(candidates: List[str], depth: int = 0):
        if depth == len(s):
            result.append(candidates[:])
        else:
            combi(candidates, depth + 1)
            combi(candidates + [s[depth]], depth + 1)

    result = []
    combi([])
    return result

if __name__ == "__main__":
    res = combination([i for i in "ABC"])
    print(res)