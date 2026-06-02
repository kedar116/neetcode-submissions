class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        min_result=float('inf')
        while(left<=right):
            result=0
            k=(left+right)//2
            for i in piles:
                result+=math.ceil(i/k)
            if result<=h:
                min_result=min(min_result,k)
                right=k-1
            else:
                left=k+1
        return min_result