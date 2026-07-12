class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0 
        intervals.sort()
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                res+=1
                prevEnd = min(prevEnd, intervals[i][1])
        return res