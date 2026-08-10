class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i==len(nums)-1:
                memo[i]=0
                return 0
            max_steps = min(len(nums)-1,i+nums[i])
            min_jumps = float("inf")
            for j in range(i+1,max_steps+1):
                min_jumps = min(min_jumps, 1+dfs(j))
                memo[i] = min_jumps
            return min_jumps

        return dfs(0)
