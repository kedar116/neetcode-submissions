class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid] < nums[right]:
                right=mid
            else:
                left=mid+1
        pivot=left


        if target >nums[-1]:
            l=0
            r=pivot-1
        else:
            l=pivot
            r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m
        return -1