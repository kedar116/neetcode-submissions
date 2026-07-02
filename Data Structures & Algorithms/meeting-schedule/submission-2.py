"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    #Brute force 1
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[i].end>intervals[j].start and intervals[j].end>intervals[i].start:
                    return False
        return True