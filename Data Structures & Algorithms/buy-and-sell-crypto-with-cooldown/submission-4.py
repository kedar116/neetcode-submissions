class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buying in [True,False]:
                if buying:
                    buy = dp[i+1][False] - prices[i]
                    cooldown = dp[i+1][True]
                    dp[i][True] = max(buy,cooldown)
                else:
                    sell = dp[i+2][True] + prices[i] if i+2<n else prices[i]
                    cooldown = dp[i+1][False]
                    dp[i][False] = max(sell,cooldown)
        return dp[0][True]

      
