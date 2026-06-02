class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap=defaultdict(int)
        if len(s1)>len(s2):
            return False
        for i in s1:
            hashmap[i]+=1

        for i in range(len(s2)):
            target=""
            target=s2[i:i+len(s1)]
            if len(target)<len(s1):
                break
            freq=defaultdict(int)
            for j in target:
                freq[j]+=1
            if freq==hashmap:
                return True
        return False
            

            