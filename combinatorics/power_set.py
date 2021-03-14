from typing import List, Set

# This is too complex. See subsets for simpler backtracking implementation.
def power_set(inn: List[str]) -> List[str]:
    """
    Generate bitset backtrack
    https://www.youtube.com/watch?v=RnlHPR0lyOE&ab_channel=WilliamFiset
    """
    def bs(i: int, bts: List[int], bs_list: List[List[int]]):
        if i == len(bts):
            bs_list.append(bts[:])
        else:
            bts[i] = 0
            bs(i + 1, bts, bs_list)
            bts[i] = 1
            bs(i + 1, bts, bs_list)

    bitset = []
    bs(0, [0] * len(inn), bitset)
    rs = []

    for bs in bitset:
        candidate = ""
        for j in range(len(bs)):
            if bs[j] == 1:
                candidate += inn[j]
        rs.append(candidate)
    return rs


"""
Same like above but just use bit shift
"""


def power_set_bit(inn: List[str]) -> List[str]:
    rs = []
    for bs in range(2**len(inn)):
        candidate = ""
        n = len(inn)
        for j in range(n):
            if 1 & (bs >> j):
                candidate += inn[j]
        rs.append(candidate)
    return rs


if __name__ == "__main__":
    print(power_set_bit([str(i) for i in "abcd"]))
