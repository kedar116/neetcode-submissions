class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #O(N*logN)
        #N for converting array into heap
        #logN for inserting into heap
        for i in range(len(stones)):
            stones[i]= -stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x!=y:
                heapq.heappush(stones, -(abs(x)-abs(y)))
        return abs(stones[0]) if stones else 0