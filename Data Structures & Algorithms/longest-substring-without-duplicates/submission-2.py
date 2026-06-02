class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=1
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        for i in range(len(s)):
            hashset =set()
            length=1
            hashset.add(s[i])
            for j in range(i+1,len(s)):
                if s[j] in hashset:
                    break
                else:
                    length+=1
                    hashset.add(s[j])
            max_length=max(length,max_length)
        return max_length
