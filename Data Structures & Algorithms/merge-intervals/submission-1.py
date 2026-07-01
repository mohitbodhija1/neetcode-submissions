class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        prev=intervals[0]
        res=[]
        for i in range(1, len(intervals)):
            curr=intervals[i]
            if prev[1]>=curr[0]:
                prev[1]=max(curr[1], prev[1])
            else:
                res.append(prev)
                prev=curr
        res.append(prev)
        return res

        