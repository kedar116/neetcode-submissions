class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        min_result = nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                min_result=min(min_result,nums[l])
                break

            m=(l+r)//2
            min_result=min(min_result,nums[m])
            if (nums[m]>=nums[l]):
                l=m+1
            else:
                r=m-1
        return min_result
