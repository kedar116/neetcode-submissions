class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right=0,0
        maxf=0
        res=0
        count=defaultdict(int)
        for right in range(len(s)):
            count[s[right]]+=1
            maxf=max(maxf,count[s[right]])
            if (right-left+1)-maxf <=k:
                res=max(res,right-left+1)
            else:
                count[s[left]]-=1
                left+=1
        return res
                


