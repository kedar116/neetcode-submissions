class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT=defaultdict(int)
        for i in t:
            countT[i]+=1
        res=[-1,-1]
        resLen=float("infinity")
        for i in range(len(s)):
            countS=defaultdict(int)
            for j in range(i,len(s)):
                countS[s[j]]+=1
                flag=True
                for k in countT:
                    if countT[k]>countS[k]:
                        flag=False
                        break
                if flag and (j-i+1)<resLen:
                    resLen=j-i+1
                    res=[i,j]
        l,r=res
        return s[l:r+1] if resLen!=float("infinity") else ""


