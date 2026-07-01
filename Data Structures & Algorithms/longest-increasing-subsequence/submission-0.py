class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Every element alone is a valid subsequence of length 1
        dp = [1] * n
        
        # For each index i, look at all previous indices j
        for i in range(1, n):
            for j in range(i):
                # Can we extend the subsequence ending at j?
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # Answer can end anywhere in the array
        return max(dp)