class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        bottom_dp = [0]*(n+1)
        for j in range(n+1):
            bottom_dp[j]=n-j
        for i in range(m-1,-1,-1):
            curr_dp = [0]*(n+1)
            curr_dp[n]=m-i
            for j in range(n-1,-1,-1):
                if word1[i]==word2[j]:
                    curr_dp[j] = bottom_dp[j+1]
                else:
                    curr_dp[j] = 1 + min(curr_dp[j+1], bottom_dp[j], bottom_dp[j+1])
            bottom_dp = curr_dp
        return bottom_dp[0]