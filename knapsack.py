# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60

from typing import List

indent_prefix = "| "

def knapsack(profits: List[int], weights: List[int], capacity: int) -> int:
    def recurse(profits: List[int], weights: List[int], capacity: int, index: int, indent: int) -> int:
        print(indent_prefix * indent + f"knapsack(cap={capacity}, idx={index})")
        if capacity <= 0 or index >= len(weights):
            return 0
        
        profit1 = 0
        if weights[index] <= capacity:
            profit1 = profits[index] + recurse(profits, weights, capacity - weights[index], index + 1, indent + 1)

        profit2 = recurse(profits, weights, capacity, index + 1, indent + 1)
        return max(profit1, profit2)

    return recurse(profits, weights, capacity, 0, 0)

"""
"""
def knapsack_memo(profits: List[int], weights: List[int], capacity: int) -> int:
    def recurse(profits: List[int], weights: List[int], capacity: int, index: int, memo: List[List[int]], indent: int) -> int:
        print(indent_prefix * indent + f"knapsack(cap={capacity}, idx={index})")

        if capacity <= 0 or index >= len(weights):
            return 0

        # memo check must be done after base case check!
        if memo[index][capacity] is not None:
            return memo[index][capacity]

        profit1 = 0
        if weights[index] <= capacity:
            profit1 = profits[index] + recurse(profits, weights, capacity - weights[index], index + 1, memo, indent + 1)

        profit2 = recurse(profits, weights, capacity, index + 1, memo, indent + 1)
        memo[index][capacity] = max(profit1, profit2)
        return memo[index][capacity]

    memo = [[None for x in range (capacity + 1)] for y in range(len(profits))]
    return recurse(profits, weights, capacity, 0, memo, 0)

if __name__ == "__main__":
    # print(knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 7)) # 22
    # print(knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 6)) # 17
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 7))