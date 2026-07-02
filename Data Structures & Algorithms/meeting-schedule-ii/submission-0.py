from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # Edge case: no meetings
        if not intervals:
            return 0
        
        # Separate and sort starts and ends independently
        starts = sorted(i.start for i in intervals)
        ends   = sorted(i.end   for i in intervals)
        
        s, e = 0, 0                    # two pointers
        rooms = 0                      # current rooms in use
        max_rooms = 0                  # answer
        
        # We only need to process all start events
        while s < len(intervals):
            
            if starts[s] < ends[e]:
                # New meeting starts before any current meeting ends
                # Must allocate a new room
                rooms += 1
                s += 1
            else:
                # A meeting has ended, free up that room
                # starts[s] >= ends[e] handles back-to-back correctly
                rooms -= 1
                e += 1
            
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms