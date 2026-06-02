class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute Force
        output=[]
        for i in range(len(nums)):
            res=1
            for j in range(len(nums)):
                if i!=j:
                    res*=nums[j]
            output.append(res)
        return output  