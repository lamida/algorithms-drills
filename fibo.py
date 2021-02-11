from typing import List
# 0, 1, 1, 2, 3, 5, ...
# fibo[0] = 0
# fibo[1] = 1
indent_prefix = "| "

"""
Recursive Fibonacci
"""
def fibo(n: int) -> int:
    def recurse(n: int, indent: int) -> int:
        # print(indent * indent_prefix + f"fibo({n})")
        if n <= 1:
            return n
        return recurse(n - 1, indent + 1) + recurse(n - 2, indent + 1)
    return recurse(n, 0)

"""
Recursive Fibonacci with memoization to reduce the exponential recursion
"""
def fibo_memo(n: int) -> int:
    def recurse(n: int, memo: List[int], indent: int) -> int:
        # print(indent * indent_prefix + f"fibo({n})")
        if memo[n] is not None:
            return memo[n]

        if n <= 1:
            memo[n] = n
        else:
            memo[n] = recurse(n - 1, memo, indent + 1) + recurse(n - 2, memo, indent + 1)
        return memo[n]
    memo = [None] * (n + 1)
    return recurse(n, memo, 0)

"""
Bottom up Fibonacci using tabulation
"""
def fibo_tab(n: int) -> int:
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

if __name__ == "__main__":
    for i in range(10):
        print(i, fibo(i), fibo_memo(i), fibo_tab(i))
