class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for ele in nums:
            if ele in hash:
                return True
            else:
                hash[ele] =1
        return False
        