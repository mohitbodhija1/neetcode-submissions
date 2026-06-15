from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # Run both Kadane's (max) and inverse Kadane's (min) in one pass
        max_sum  = nums[0]
        curr_max = nums[0]
        
        min_sum  = nums[0]
        curr_min = nums[0]
        
        total = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            total += num
            
            # Normal Kadane's for max subarray
            curr_max = max(num, curr_max + num)
            max_sum  = max(max_sum, curr_max)
            
            # Inverse Kadane's for min subarray
            curr_min = min(num, curr_min + num)
            min_sum  = min(min_sum, curr_min)
        
        # Edge case: all numbers negative
        # total - min_sum would give 0 (empty array), not valid
        if max_sum < 0:
            return max_sum
        
        # Case 1: normal max,  Case 2: circular max
        return max(max_sum, total - min_sum)