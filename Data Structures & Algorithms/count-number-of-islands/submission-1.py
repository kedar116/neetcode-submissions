class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows,cols = len(grid), len(grid[0])
        visited = set()
        islands=0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    if ((r+dr) in range(rows) and (c+dc) in range(cols)
                        and grid[r+dr][c+dc]=="1" 
                        and (r+dr,c+dc) not in visited):
                        q.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1

        return islands
        