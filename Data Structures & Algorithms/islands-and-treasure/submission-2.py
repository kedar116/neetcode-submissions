class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited=set()
            distance = 0
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    if grid[row][col] == 0:
                        return distance
                    for dr,dc in directions:                                            
                        if ((row+dr) in range(rows) and (col+dc) in range(cols)
                            and grid[row+dr][col+dc]!=-1) and (row+dr,col+dc) not in visited:
                            visited.add((row+dr,col+dc))
                            q.append((row+dr,col+dc))
                distance+=1
            return INF

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==INF:
                    grid[r][c] = bfs(r,c)