class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        l=len(heights)-1
        max_area=0
        while i<=l:
            width = l-i
            height = min(heights[i], heights[l])
            max_area= max(max_area, width*height)
            if heights[i]>heights[l]:
                l-=1
            else:
                i +=1
        return max_area

        