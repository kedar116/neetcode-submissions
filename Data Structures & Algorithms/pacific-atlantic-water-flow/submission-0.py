class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #brute force
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        result = []


        def bfs(r,c):
            visited = set()  
            q = deque()
            q.append ((r,c))
            visited.add((r,c))
            pacific = False
            atlantic = False
            while q:
                row, col = q.popleft()
                if row==0 or col==0:
                    pacific = True
                if row==ROWS-1 or col==COLS-1:
                    atlantic = True
                if pacific and atlantic:
                    return True

                for dr, dc in directions:
                    if ((row+dr) in range(ROWS) and (col+dc) in range(COLS) 
                        and ((row+dr, col+dc)) not in visited
                        and heights[row+dr][col+dc] <= heights[row][col]):
                        q.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if bfs(r,c):
                    result.append([r,c])

        return result

        


