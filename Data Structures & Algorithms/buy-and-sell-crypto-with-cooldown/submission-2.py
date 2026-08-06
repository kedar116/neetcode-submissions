class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        memo=[[None]*2 for _ in range(n)]
        def dfs(i,buying):
            if i>=len(prices):
                return 0
            if memo[i][buying]!=None:
                return memo[i][buying]
            if buying:
                buy = dfs(i+1,False) - prices[i]
                cooldown = dfs(i+1,buying)
                memo[i][buying] = max(buy,cooldown)
            else:
                sell = dfs(i+2,True)+prices[i]
                cooldown = dfs(i+1,buying)
                memo[i][buying] = max(sell,cooldown)
            return memo[i][buying]
        return dfs(0,True)
