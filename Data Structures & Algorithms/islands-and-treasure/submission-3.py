class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Multi source BFS(optimal)
        rows , cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        visited=set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        distance=1
        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    if ((row+dr) in range(rows) and (col+dc) in range(cols)
                        and (row+dr,col+dc) not in visited 
                        and grid[row+dr][col+dc]!=-1):
                        grid[row+dr][col+dc]=distance
                        q.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))
            distance+=1
