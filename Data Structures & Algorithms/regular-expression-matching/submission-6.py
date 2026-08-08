class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        bottom_dp = [False]*(n+1)
        bottom_dp[n] = True
        for i in range(m,-1,-1):
            current_dp = [False]*(n+1)
            current_dp[n] = (i==m)
            for j in range(n-1,-1,-1):
                match = i<m and (s[i]==p[j] or p[j]==".")
                if (j+1)<n and p[j+1]=="*":
                    current_dp[j] = current_dp[j+2] or (match and bottom_dp[j])
                elif match:
                    current_dp[j]=bottom_dp[j+1]
                else:
                    current_dp[j]=False
            bottom_dp = current_dp

        return bottom_dp[0]
