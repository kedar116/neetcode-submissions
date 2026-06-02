class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        heap=[]
        heapq.heapify(heap)
        for i in hashmap:
            heapq.heappush(heap,(hashmap[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        while k>0:
            result.append(heapq.heappop(heap)[1])
            k-=1
        return result