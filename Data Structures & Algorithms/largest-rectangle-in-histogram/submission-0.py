class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=-9999999999
        for i in range(len(heights)):
            left=i-1
            right=i+1
            while left>=0: 
                if heights[i]<=heights[left]:
                    left-=1
                else:
                    break
            while right<=len(heights)-1:
                if heights[i]<=heights[right]:
                    right+=1
                else:
                    break
            area=(right-left-1)*heights[i]
            max_area=max(max_area, area)
        return max_area
