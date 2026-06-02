class MedianFinder:

    def __init__(self):
        self.res = []
        self.total = 0

    def addNum(self, num: int) -> None:
        self.res.append(num)
        self.total+=1
        self.res.sort()

    def findMedian(self) -> float:
        n = len(self.res)
        if self.total % 2 ==0:
            median = (self.res[n//2] + self.res[(n//2)-1])/2
        else:
            median = self.res[n//2]
        return median

        
        