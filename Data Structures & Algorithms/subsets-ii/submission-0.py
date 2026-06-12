class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res=set()
        nums.sort()
        
        def dfs(i):
            if i>=len(nums):
                res.add(tuple(subset.copy()))
                return
            #select
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return [list(subset) for subset in res]