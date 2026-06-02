class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        count=0
        while True:
            stones.sort()
            if count==len(stones):
                return 0
            if count==len(stones)-1:
                return stones[-1]
            n=len(stones)
            x = stones[n-1]
            y = stones[n-2]
            if x==y:
                stones[n-1]=0
                stones[n-2]=0
                count+=2
            else:
                stones[n-2]=abs(x-y)
                stones[n-1]=0
                count+=1
                  