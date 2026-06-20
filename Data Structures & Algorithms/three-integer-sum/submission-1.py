from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):  # -2 because s and e need atleast 2 elements after i

            # Skip duplicate values for i
            # e.g [-1,-1,0,1] when i=1, nums[1]==nums[0] so skip
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Early termination — if smallest element > 0, no triplet possible
            if nums[i] > 0:
                break

            s = i + 1
            e = n - 1

            while s < e:
                total = nums[i] + nums[s] + nums[e]

                if total == 0:
                    res.append([nums[i], nums[s], nums[e]])  # ← Fix: values not indices

                    # Skip duplicates for s
                    # e.g [0,0,0,1] after match, s=0 and nums[s+1]=0 so skip
                    while s < e and nums[s] == nums[s+1]:
                        s += 1
                    # Skip duplicates for e
                    while s < e and nums[e] == nums[e-1]:
                        e -= 1

                    s += 1  # Move both pointers after handling duplicates
                    e -= 1

                elif total > 0:
                    e -= 1
                else:
                    s += 1

        return res


# Tests
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))   # [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0, 0, 0, 0]))             # [[0,0,0]]
print(sol.threeSum([-2, 0, 0, 2, 2]))         # [[-2,0,2]]
print(sol.threeSum([1, 2, 3]))                # []  (no negatives)
print(sol.threeSum([-1, -1, -1, 0, 1, 2]))   # [[-1,-1,2],[-1,0,1]]