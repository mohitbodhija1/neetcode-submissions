class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest =0
        for num in nums:
            if num-1 not in num_set:
                #this can be a start point
                curr=num
                streak=1

                while curr+1 in num_set:
                    curr+=1
                    streak +=1
                longest=max(longest, streak)
        return longest