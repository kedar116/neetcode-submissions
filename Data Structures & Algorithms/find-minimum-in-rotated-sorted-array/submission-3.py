class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        min_num=9999999
        while left<=right:
            if nums[left] <nums[right]:
                min_num=min(min_num, nums[left])
                break
                
            mid=(left+right)//2
            min_num=min(min_num,nums[mid])
            if nums[mid]>=nums[left]:
                left=mid+1
            else:
                right=mid-1
        return min_num        