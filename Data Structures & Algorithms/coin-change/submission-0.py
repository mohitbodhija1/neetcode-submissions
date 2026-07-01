from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[a] = minimum coins needed to make amount a
        # Initialize with amount+1 as "infinity" (can never need more coins than amount)
        dp = [float('inf')] * (amount + 1)

        # Base case: 0 coins needed to make amount 0
        dp[0] = 0

        for a in range(1, amount + 1):          # every amount from 1 to target
            for coin in coins:                  # try every coin
                if a - coin >= 0:               # can we use this coin?
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        # If dp[amount] is still infinity, it's impossible
        return dp[amount] if dp[amount] != float('inf') else -1