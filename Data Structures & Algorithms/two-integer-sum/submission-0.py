class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash ={}
        i=0
        for ele in nums:
            if target-ele not in hash:
                hash[ele] =i
            else:
                return [hash[target-ele], i]
            i +=1
        