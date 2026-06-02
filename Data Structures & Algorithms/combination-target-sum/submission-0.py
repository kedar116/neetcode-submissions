class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        subsets=[]

        def dfs(i,total):
            if i>=len(nums) or total > target:
                return

            if total == target:
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i, total+nums[i])

            subsets.pop()
            dfs(i+1, total)

        dfs(0,0)

        return res
