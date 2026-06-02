class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))

        while q and fresh>0:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    if (row+dr) in range(rows) and (col+dc) in range(cols)and grid[row+dr][col+dc]==1:
                        grid[row+dr][col+dc]=2
                        q.append((row+dr,col+dc))
                        fresh-=1
            minutes+=1

        return minutes if fresh==0 else -1
