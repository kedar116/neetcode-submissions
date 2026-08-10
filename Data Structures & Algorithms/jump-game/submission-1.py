class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None]*len(nums)
        def dfs(i):
            if memo[i]is not None:
                return memo[i]
            if i==len(nums)-1:
                memo[i]= True
                return True
        
            end = min(len(nums)-1,i+nums[i])
            for j in range(i+1,end+1):
                if dfs(j):
                    memo[i]=True
                    return True
            memo[i] = False
            return False
        return dfs(0)