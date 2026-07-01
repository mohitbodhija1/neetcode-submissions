class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1: Build a m x n DP table filled with 1s
        # Base case: entire first row and first column are 1
        dp = [[1] * n for _ in range(m)]

        # Step 2: Fill interior cells using the recurrence
        # paths(i,j) = paths(i-1,j) + paths(i,j-1)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Step 3: Bottom-right corner holds the final answer
        return dp[m - 1][n - 1]