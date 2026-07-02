"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #Brute force 2
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if min(intervals[i].end, intervals[j].end)>max(intervals[i].start,intervals[j].start):
                    return False
        return True