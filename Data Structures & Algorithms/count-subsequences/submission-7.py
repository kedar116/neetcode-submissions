class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        bottom_row =[0]*(n+1)
        bottom_row[n]=1

        for i in range(m-1,-1,-1):
            current_row = [0]*(n+1)
            current_row[n]=1
            for j in range(n-1,-1,-1):
                if s[i]==t[j]:
                    current_row[j] = bottom_row[j] + bottom_row[j+1]
                else:
                    current_row[j] = bottom_row[j]
            bottom_row = current_row
        return bottom_row[0]

        