class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo=[None]*(len(s)+1)
        def dfs(i):
            if i==len(s):
                return True
            if memo[i] is not None:
                return memo[i]
            for w in wordDict:
                if (i+len(w)<=len(s) and s[i:i+len(w)]==w):
                    if dfs(i+len(w)):
                        memo[i]=True
                        return True
            memo[i]=False
            return False

        return dfs(0)
            