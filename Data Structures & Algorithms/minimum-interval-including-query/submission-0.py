class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        for i in range(len(queries)):
            length = 0
            min_length = 99999
            for j in range(len(intervals)):
                left = intervals[j][0]
                right = intervals[j][1]
                if left<=queries[i]<=right:
                    length = right-left+1
                    min_length = min(length, min_length)
            if min_length==99999:
                output.append(-1)  
            else:
                output.append(min_length)
        return output