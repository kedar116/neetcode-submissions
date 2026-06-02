class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            x=stones.pop()
            y=stones.pop()
            if x-y!=0:
                stones.append(abs(x-y))
        return stones[0] if stones else 0