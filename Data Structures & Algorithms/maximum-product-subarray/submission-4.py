class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin=1,1
        res=max(nums)
        for num in nums:
            if num==0:
                curMax,curMin=1,1
            temp=num*curMax
            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,num*curMin,num)
            res=max(res,curMax)
        return res

