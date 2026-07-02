class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        s=((l)*(l+1))//2
        curr=sum(nums)
        return s-curr
        