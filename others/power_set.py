# Not done yet
from typing import List, Set


def power_set(inn: List[int]) -> List[int]:
    res = []
    if len(inn) == 0:
        return []
    for i in range(len(inn)):
        n = inn[i]
        nn = power_set(inn[i+1:])
        res += [[n] + nn]
        res += [nn]
    return res

if __name__ == "__main__":
    print(power_set([1, 2]))
