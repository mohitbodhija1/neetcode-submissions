import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:               # loop ends when lo == hi == answer
            mid = (lo + hi) // 2
            
            # hours needed at speed mid
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours <= h:
                hi = mid             # mid is feasible, but maybe smaller works
            else:
                lo = mid + 1         # too slow, must go faster

        return lo