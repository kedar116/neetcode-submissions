class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        target=sum(nums)//2
        memo=[[-1]*(target+1)for _ in range(n+1)]

        if sum(nums)%2!=0:
            return False
        
        def dfs(i,target):
            if i>=len(nums):
                return target==0
            if target<0:
                return False
            if memo[i][target]!=-1:
                return memo[i][target]
            memo[i][target] = dfs(i+1,target) or dfs(i+1,target-nums[i])
            return memo[i][target]
        return dfs(0,target)