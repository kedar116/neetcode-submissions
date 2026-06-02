class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #BFS
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area=0

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            area=1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    if ((row+dr) in range(rows) and (col+dc) in range(cols)
                        and (row+dr,col+dc) not in visited 
                        and grid[row+dr][col+dc]==1):
                        area+=1
                        q.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        return max_area
        

        

