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

        
#BruteForce DFS
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         ROWS, COLS = len(heights), len(heights[0])
#         result = []

#         def reach_pacific(r, c, visited):
#             # Base Case 1: If we touch the Pacific boundary, we made it!
#             if r == 0 or c == 0:
#                 return True
            
#             visited.add((r, c))
            
#             # Explore neighbors downhill
#             for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
#                 nr, nc = r + dr, c + dc
#                 if (nr in range(ROWS) and nc in range(COLS) 
#                     and (nr, nc) not in visited
#                     and heights[nr][nc] <= heights[r][c]):
                    
#                     # If any neighbor path reaches the Pacific, return True
#                     if reach_pacific(nr, nc, visited):
#                         return True
#             return False

#         def reach_atlantic(r, c, visited):
#             # Base Case 1: If we touch the Atlantic boundary, we made it!
#             if r == ROWS - 1 or c == COLS - 1:
#                 return True
            
#             visited.add((r, c))
            
#             # Explore neighbors downhill
#             for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
#                 nr, nc = r + dr, c + dc
#                 if (nr in range(ROWS) and nc in range(COLS) 
#                     and (nr, nc) not in visited
#                     and heights[nr][nc] <= heights[r][c]):
                    
#                     # If any neighbor path reaches the Atlantic, return True
#                     if reach_atlantic(nr, nc, visited):
#                         return True
#             return False

#         # Main Loop
#         for r in range(ROWS):
#             for c in range(COLS):
#                 # We need a fresh visited set for each independent ocean check
#                 if reach_pacific(r, c, set()) and reach_atlantic(r, c, set()):
#                     result.append([r, c])

#         return result

