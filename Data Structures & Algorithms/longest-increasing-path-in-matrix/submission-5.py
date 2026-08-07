class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS,COLS = len(matrix), len(matrix[0])
        directions = [[-1,0],[0,1],[0,-1],[1,0]]
        dp = {} # (r,c) -> LIP

        def dfs(r,c, prevVal):
            if r<0 or r==ROWS or c<0 or c==COLS or matrix[r][c]<=prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1
            # for dr, dc in directions:
            #     res = max(res, 1+dfs(r+dr,c+dc,matrix[r][c]))
            res=max(res,1+dfs(r+1,c,matrix[r][c]))
            res=max(res,1+dfs(r-1,c,matrix[r][c]))
            res=max(res,1+dfs(r,c+1,matrix[r][c]))
            res=max(res,1+dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        LIP =0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r,c,float('-inf')))
        return LIP