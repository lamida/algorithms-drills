from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        
        return -1 if dp[amount] > amount else dp[amount]


if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    s = Solution()
    res = s.coinChange(coins, amount)
    print(res)
