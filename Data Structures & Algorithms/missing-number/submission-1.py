class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
        # l=len(nums)
        # s=((l)*(l+1))//2
        # curr=sum(nums)
        # return s-curr
        
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        xor = 0
        
        for i in range(n + 1):
            xor ^= i          # XOR with every index 0..n
            if i < n:
                xor ^= nums[i]  # XOR with every value in nums
        
        # All present numbers cancel out, missing number survives
        return xor

