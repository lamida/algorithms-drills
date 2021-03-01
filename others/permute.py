from typing import List

"""
Just print permutation
"""
def permute(s: str):
    def permute(a: List[str], l: int, r: int):
        if l == r:
            print(a)
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                permute(a, l + 1, r)
                a[l], a[i] = a[i], a[l]
    return permute([str(i) for i in "ABC"], 0, len(s) - 1)

"""
Return the list of permutation
"""
def permute2(s: str) -> List[str]:
    def permute(a: List[str], l: int, r: int, ll: List[List[str]]):
        if l == r:
            ll.append("".join(a))
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                permute(a, l + 1, r, ll)
                a[l], a[i] = a[i], a[l]
    ll = []
    permute([str(i) for i in "ABC"], 0, len(s) - 1, ll)
    return ll

if __name__ == "__main__":
    x = permute2("ABC")
    print(x)

