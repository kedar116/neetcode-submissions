class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows,cols = len(grid), len(grid[0])
        visited = set()
        islands=0

        def dfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row,col = q.pop()
                for dr,dc in directions:
                    if ((row+dr) in range(rows) and (col+dc) in range(cols)
                        and grid[row+dr][col+dc]=="1" 
                        and (row+dr,col+dc) not in visited):
                        q.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    dfs(r,c)
                    islands+=1

        return islands
        