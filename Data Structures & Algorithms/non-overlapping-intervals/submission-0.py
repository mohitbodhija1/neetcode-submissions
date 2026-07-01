class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        # Sort intervals by end time (greedy choice)
        intervals.sort(key=lambda x: x[1])

        # Always keep the first interval (ends earliest)
        last_end = intervals[0][1]
        removals = 0

        # Process remaining intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last_end:
                # Overlap detected — remove the interval ending later
                # Since sorted by end, current end >= last_end
                # So we remove current interval (implicitly, by not updating last_end)
                removals += 1

            else:
                # No overlap — keep this interval, move last_end forward
                last_end = end

        return removals