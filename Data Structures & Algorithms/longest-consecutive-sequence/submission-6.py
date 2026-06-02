class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        s=set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
        nums=list(s)
        nums.sort()
        max_count=1
        count=1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            else:
                count=1
            max_count=max(count,max_count)
        return max_count
