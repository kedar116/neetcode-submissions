class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        left,right=[-1]*len(heights), [len(heights)]*len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            stack.append(i)

        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)

        maxarea=0
        for i in range(len(heights)):
            maxarea=max(maxarea, (right[i]-left[i]-1)*heights[i])

        return maxarea