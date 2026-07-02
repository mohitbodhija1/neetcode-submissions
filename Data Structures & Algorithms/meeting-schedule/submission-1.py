"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        n=len(intervals)
        if n==0:
            return True
        prev=intervals[0]
        for i in range(1,n):
            curr=intervals[i]
            if prev.end>curr.start:
                return False
            prev=curr
        return True
