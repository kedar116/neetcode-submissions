class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #O(a*c), O(a)
        m, n = len(coins), amount
        bottomRow = [0]*(n+1)
        bottomRow[n] = 1

        for i in range(m-1,-1,-1):
            currRow = [0]*(n+1)
            currRow[n]=1
            for j in range(n-1,-1,-1):
                skip = bottomRow[j]
                take = currRow[j+coins[i]] if j+coins[i]<=n else 0
                currRow[j] = skip+take

            bottomRow = currRow
        return bottomRow[0]