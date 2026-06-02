class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1

        freq=[[] for i in range(len(nums)+1)]
        for i in hashmap:
            freq[hashmap[i]].append(i)
        output=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                output.append(j)
                if len(output)==k:
                    return output
        