class MedianFinder:

    # O(N),O(N)

    def __init__(self):
        self.res = []
        self.total = 0

    def addNum(self, num: int) -> None:
        self.total+=1
        for i in range(len(self.res)):
            if num <= self.res[i]:
                self.res.insert(i,num)
                return
        self.res.append(num)

    def findMedian(self) -> float:
        n = len(self.res)
        if self.total % 2 ==0:
            median = (self.res[n//2] + self.res[(n//2)-1])/2
        else:
            median = self.res[n//2]
        return median

        
        