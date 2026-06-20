from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # Step 1: Build left max array
        # left[i] = max height from index 0 to i (inclusive)
        left = [0] * n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])

        # Step 2: Build right max array
        # right[i] = max height from index i to n-1 (inclusive)
        right = [0] * n
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):          # ← Fix: n-2 to 0
            right[i] = max(height[i], right[i+1])  # ← Fix: height[i] not ele

        # Step 3: Calculate water at each index
        max_water = 0
        for i in range(n):
            water_at_i = min(left[i], right[i]) - height[i]
            max_water += water_at_i

        return max_water