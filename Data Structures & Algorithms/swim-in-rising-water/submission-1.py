class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        minHeap = [] #elevation,r,c
        heapq.heappush(minHeap, (grid[0][0],0,0))
        visit.add((0,0))
        
        while minHeap:
            elevation,r,c = heapq.heappop(minHeap)
            if r==ROWS-1 and c==COLS-1:
                return elevation
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    heapq.heappush(minHeap,(max(elevation,grid[nr][nc]),nr,nc))

        return -1