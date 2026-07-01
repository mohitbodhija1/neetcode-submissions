class Solution:
    def robResult(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        prev1, prev2=nums[0], 0
        for i in range(2,n+1):
            curr=max(prev1, prev2+nums[i-1])
            prev2=prev1
            prev1=curr
        return prev1
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        first = self.robResult(nums[:n-1])
        last = self.robResult(nums[1:])
        return max(first,last)

        