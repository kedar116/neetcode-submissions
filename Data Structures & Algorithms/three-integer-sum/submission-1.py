class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_s=set()
        res=[]
        #hashmap=defaultdict(int)
        nums.sort()
        for i in range(len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                temp=-(nums[i]+nums[j])
                if temp in seen:
                    res_s.add((nums[i],temp,nums[j]))
                seen.add(nums[j])

        for i in res_s:
            res.append(list(i))
        return res


        