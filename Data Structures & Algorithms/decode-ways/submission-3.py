class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        next1=1
        next2=0
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                current=0
            else:
                current=next1
                if i<n-1 and (s[i]=="1" or s[i]=="2" and s[i+1]<"7"):
                    current+=next2
            next2=next1
            next1=current
        return next1
