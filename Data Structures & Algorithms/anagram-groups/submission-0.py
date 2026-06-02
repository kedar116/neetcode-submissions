class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        def validAnagram(str1,str2):
            count=defaultdict(int)
            for i in str1:
                count[i]+=1
            for i in str2:
                count[i]-=1
            for i in count:
                if count[i]!=0:
                    return False
            return True

        for s in strs:
            flag=False
            for group in output:
                if validAnagram(group[0],s):
                    group.append(s)
                    flag=True
                    break
            if not flag:
                output.append([s])

        return output

            

                    
                
        