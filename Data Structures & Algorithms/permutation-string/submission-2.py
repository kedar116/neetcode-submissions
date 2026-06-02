class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1=defaultdict(int)
        hashmap2=defaultdict(int)
        left,right=0,0
        for i in s1:
            hashmap1[i]+=1
        for right in range(len(s2)):
            hashmap2[s2[right]]+=1
            if right-left+1 > len(s1):
                hashmap2[s2[left]]-=1
                if hashmap2[s2[left]]==0:
                    del hashmap2[s2[left]]
                left+=1
            if (right-left+1)==len(s1) and hashmap1==hashmap2:
                return True
        return False


