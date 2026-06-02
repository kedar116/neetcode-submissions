class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        dict2={}
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]]+=1
            else:
                dict1[s[i]]=1

        for j in range(len(t)):
            if t[j] in dict2:
                dict2[t[j]]+=1
            else:
                dict2[t[j]]=1

        if dict1==dict2:
            return True
        else:
            return False
        
