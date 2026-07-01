class Solution:
    def rob(self, nums: List[int]) -> int:
        # n=len(nums)
        # if n==1:
        #     return nums[0]
        # dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=nums[0]
        # for i in range(2,n+1):
        #     dp[i]= max(dp[i-1], dp[i-2]+nums[i-1])
        # return dp[-1]
        n=len(nums)
        if n==1:
            return nums[0]
        prev1, prev2=nums[0], 0
        for i in range(2,n+1):
            curr=max(prev1, prev2+nums[i-1])
            prev2=prev1
            prev1=curr
        return prev1

        