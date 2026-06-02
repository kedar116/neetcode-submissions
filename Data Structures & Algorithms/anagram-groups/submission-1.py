class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        output=[]
        for i in strs:
            key=''.join(sorted(i))
            if key not in hashmap:
                hashmap[key]=[i]
            else:
                hashmap[key].append(i)
        for i in hashmap:
            output.append(hashmap[i])
        return output

        