class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS, COLS = len(board), len(board[0])

        def capture(r,c):
            q = deque()
            q.append((r,c))
            board[r][c]='T'
            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if nr in range(ROWS) and nc in range(COLS) and board[nr][nc]=='O':
                        board[nr][nc]='T'
                        q.append((nr,nc))
                

        for c in range(COLS):
            if board[0][c]=='O':
                capture(0,c)
            if board[ROWS-1][c]=='O':
                capture(ROWS-1,c)

        for r in range(ROWS):
            if board[r][0]=='O':
                capture(r,0)
            if board[r][COLS-1]=='O':
                capture(r,COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O':
                    board[r][c]='X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='T':
                    board[r][c]='O'