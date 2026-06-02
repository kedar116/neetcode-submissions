class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        output=[]
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        while k >0:
            max=-999999999
            for i in hashmap:
                if hashmap[i]>max:
                    max=hashmap[i]
                    max_key=i
            output.append(max_key)
            del hashmap[max_key]
            k-=1
        return output
            
        