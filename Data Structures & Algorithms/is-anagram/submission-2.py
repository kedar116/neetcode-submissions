class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=defaultdict(int)
        if len(s)!=len(t):
            return False

        for i in s:
            count[i]+=1
        for i in t:
            count[i]-=1
        for i in count:
            if count[i]!=0:
                return False
        return True
        