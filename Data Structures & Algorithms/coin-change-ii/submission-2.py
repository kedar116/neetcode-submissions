class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount
        # Base Case 1: If amount_so_far == amount (j == n), we found 1 valid combination
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n]=1 

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                skip = dp[i+1][j] 
                take = dp[i][j+coins[i]] if j+coins[i]<=n else 0
                dp[i][j] = skip+take

        return dp[0][0]




        # memo = [[-1] * amount for _ in range(len(coins))]
        # def dfs(i,amount_so_far):
        #     if amount_so_far > amount or i==len(coins):
        #         return 0
        #     if amount_so_far == amount:
        #         return 1
        #     if memo[i][amount_so_far]!=-1:
        #         return memo[i][amount_so_far]
        #     memo[i][amount_so_far] =  dfs(i+1,amount_so_far) + dfs(i,amount_so_far+coins[i])
        #     return memo[i][amount_so_far]

        # return dfs(0,0)