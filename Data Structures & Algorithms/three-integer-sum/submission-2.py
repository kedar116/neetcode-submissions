class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            seen=set()
            for j in range(i+1,len(nums)):
                if target-nums[j] in seen:
                    res.add(tuple(sorted((nums[i], target-nums[j], nums[j]))))
                seen.add(nums[j])

        return [list(t) for t in res]
        