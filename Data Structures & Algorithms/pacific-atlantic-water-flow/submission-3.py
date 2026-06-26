class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        pac, atl = set(), set()
        result = []

        def bfs(start, visited):
            q = deque(start)
            for r,c in start:
                visited.add((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr,nc = row+dr, col+dc
                    if (nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited
                        and heights[nr][nc] >= heights[row][col]):
                        visited.add((nr,nc))
                        q.append((nr,nc)) 

        pac_starts = []
        atl_starts = [] #Collecting points for multi source BFS

        for c in range(COLS):
            pac_starts.append((0,c))
            atl_starts.append((ROWS-1,c))

        for r in range(ROWS):
            pac_starts.append((r,0))
            atl_starts.append((r,COLS-1))

        bfs(pac_starts, pac)
        bfs(atl_starts, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result