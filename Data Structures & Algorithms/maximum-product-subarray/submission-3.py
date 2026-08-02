class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin=1,1
        res=float("-inf")
        for num in nums:
            temp=num*curMax
            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,num*curMin,num)
            res=max(res,curMax)
        return res

