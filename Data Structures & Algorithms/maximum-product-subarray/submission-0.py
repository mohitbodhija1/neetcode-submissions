class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        for i in range(1, len(nums)):
            ele = nums[i]
            if ele<0:
                curr_max, curr_min= curr_min, curr_max
            
            curr_max= max(curr_max*ele, ele)
            curr_min= min(ele, curr_min*ele)
            max_prod = max(curr_max,max_prod)
        return max_prod