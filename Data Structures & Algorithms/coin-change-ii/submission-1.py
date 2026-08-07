class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * amount for _ in range(len(coins))]
        def dfs(i,amount_so_far):
            if amount_so_far > amount or i==len(coins):
                return 0
            if amount_so_far == amount:
                return 1
            if memo[i][amount_so_far]!=-1:
                return memo[i][amount_so_far]
            memo[i][amount_so_far] =  dfs(i+1,amount_so_far) + dfs(i,amount_so_far+coins[i])
            return memo[i][amount_so_far]

        return dfs(0,0)