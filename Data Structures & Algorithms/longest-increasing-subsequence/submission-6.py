class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        heads=[]
        heads.append(nums[-1])
        def binary_search(arr,x):
            left,right=0,len(arr)-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]>x:
                    left=mid+1
                elif arr[mid]<x:
                    right=mid-1
                else:
                    return mid
            return left

        for i in range(len(nums)-1,-1,-1):
            x=nums[i]
            idx=binary_search(heads,x)
            if x<heads[-1]:
                heads.append(x) #You found a new large head.(Found a longer subsequence)
            else:
                heads[idx]=x
        return len(heads)
