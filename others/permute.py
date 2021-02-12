from typing import List
l = []
def permute(a: List[bytearray], l: int, r: int):
    if l == r:
        l += [a]
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

if __name__ == "__main__":
    x = permute(bytearray("ABC"), 0, 2)
    print(x)

