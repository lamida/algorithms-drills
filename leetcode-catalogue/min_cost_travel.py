# https://leetcode.com/problems/minimum-cost-for-tickets/

option = {
    1: 650,
    7: 1200,
    14: 1900,
    30: 2300,
}

def longestConsecutive(days, start) -> int:
    i = start
    if (len(days) - start) > 1:
        while i < len(days)-1 and days[i+1] - days[i] == 1:
            i += 1
        return i - start + 1
    return 1

def min_cost(days):
    cost = 0
    i = 0
    while i < len(days):
        nx = longestConsecutive(days, i)
        if nx < 7:
            cost += (nx * option[1])
        else:
            cost += option[nx]
        i += nx
    return cost

from functools import lru_cache

def mincostTickets(days, costs=[650, 1200, 1900, 2300]):
    dayset = set(days)
    durations = [1, 7, 14, 30]

    @lru_cache(None)
    def dp(i):
        if i > 365:
            return 0
        elif i in dayset:
            return min(dp(i + d) + c
                        for c, d in zip(costs, durations))
        else:
            return dp(i + 1)

    return dp(1)

if __name__ == "__main__":
    print(min_cost([1,2,3,4,5,6,7,15])) # must be 1850
    print(mincostTickets([1,2,3,4,5,6,7,15])) # must be 1850
    print(min_cost([1,2,3,4,5,6,7,13,15,17,19,20,33,201,203,205, 219])) # 4800
    print(mincostTickets([1,2,3,4,5,6,7,13,15,17,19,20,33,201,203,205, 219])) # 4800
    # 1..7..20: 2300
    # 33: 650
    # 201: 650
    # 203..219: 2
    