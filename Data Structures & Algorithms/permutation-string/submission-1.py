class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=[0]*26
        if len(s1)>len(s2):
            return False
        for i in s1:
            count1[ord(i)-ord('a')]+=1

        for i in range(len(s2)):
            target=""
            target=s2[i:i+len(s1)]
            if len(target)<len(s1):
                break
            count2=[0]*26
            for j in target:
                count2[ord(j)-ord('a')]+=1
            if count1==count2:
                return True
        return False
            

            