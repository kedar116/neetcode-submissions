class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        indegree = [[0]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                for dr,dc in directions:
                    nr,nc = (r+dr),(c+dc)
                    if 0<=nr<ROWS and 0<=nc<COLS and matrix[nr][nc]<matrix[r][c]:
                        indegree[r][c]+=1

        #BFS topological sort
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c]==0:
                    q.append([r,c])

        LIS =0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = (r+dr),(c+dc)
                    if 0<=nr<ROWS and 0<=nc<COLS and matrix[nr][nc]>matrix[r][c]:
                        indegree[nr][nc]-=1
                        if indegree[nr][nc]==0:
                            q.append([nr,nc])
            LIS+=1
        return LIS