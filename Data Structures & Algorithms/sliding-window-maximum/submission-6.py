class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        output=[]
        left=right=0
        for right in range(len(nums)):
            heapq.heappush(heap,(-nums[right],right))
            if (right+1)>=k:
                while heap[0][1]<left:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
                left+=1
        return output





