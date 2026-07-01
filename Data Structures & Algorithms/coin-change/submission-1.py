from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float('inf')

        # t[i][j] = min coins using first i coins to make amount j
        t = [[INF] * (amount + 1) for _ in range(n + 1)]

        # Base case: amount 0 always needs 0 coins
        for i in range(n + 1):
            t[i][0] = 0

        # Base case: 0 coins can't make any amount > 0
        # (already INF from initialization)

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i-1] <= j:
                    # Option 1: skip this coin → t[i-1][j]
                    # Option 2: use this coin → t[i][j-coin] + 1
                    #           ↑ same row i because unbounded (reuse allowed)
                    take = t[i][j - coins[i-1]]
                    if take != INF:              # avoid INF + 1 overflow
                        t[i][j] = min(t[i-1][j], take + 1)
                    else:
                        t[i][j] = t[i-1][j]
                else:
                    # Coin too large, skip it
                    t[i][j] = t[i-1][j]

        return t[n][amount] if t[n][amount] != INF else -1


print(Solution().coinChange([1, 2, 3], 5))   # 2
print(Solution().coinChange([1, 5, 10], 11)) # 2
print(Solution().coinChange([2], 3))         # -1