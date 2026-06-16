class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right = [0 for i in range(len(nums))]
        f=1
        last=1
        for ele in nums:
            left.append(last)
            last=ele*last
        for i in range(len(nums)-1,-1,-1):
            right[i]=f
            f=f*nums[i]
        final = []
        for i in range(len(nums)):
            final.append(left[i]*right[i])
        return final


        