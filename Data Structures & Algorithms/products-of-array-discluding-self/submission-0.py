class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=1
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                res*=nums[i]
            if nums[i]==0:
                count+=1

        output=[]
        for i in range(len(nums)):
            if count>1:
                return [0]*len(nums)
            if count==0:
                output.append(res//nums[i])
            else:
                if nums[i]==0:
                    output.append(res)
                else:
                    output.append(0)
            
        return output

        