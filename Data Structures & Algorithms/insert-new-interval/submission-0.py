from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Case 1: All intervals that end before newInterval starts — no overlap
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Case 3: Merge all overlapping intervals into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Flush the merged interval
        result.append(newInterval)

        # Case 2: All remaining intervals start after newInterval ends — no overlap
        while i < n:
            result.append(intervals[i])
            i += 1

        return result