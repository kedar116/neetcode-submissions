class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sorting
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        arr=[]
        for i in hashmap:
            arr.append([hashmap[i],i])
        arr.sort()

        result=[]
        while k>0:
            result.append(arr.pop()[1])
            k-=1
        return result