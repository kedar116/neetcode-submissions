class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_array=[0]*len(nums)
        for i in range(len(nums)):
            if new_array[nums[i]-1]==1:
                return nums[i]
            new_array[nums[i]-1]=1