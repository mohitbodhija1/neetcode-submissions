from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # dp[n] is the "top floor"
        
        # Base cases: steps 0 and 1 are free to start from
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n + 1):
            # To reach step i, you either:
            #   came from step i-1 and paid cost[i-1]
            #   came from step i-2 and paid cost[i-2]
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]