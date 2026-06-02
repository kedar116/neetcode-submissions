class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            curr=target-nums[i]
            if curr not in map:
                map[nums[i]]=i
            else:
                return [map[curr],i]