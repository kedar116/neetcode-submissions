class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        colSet = set()
        posDiag = set() #r+c
        negDiag = set() #r-c

        def backtrack(r):
            if r>=n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in colSet or (c+r) in posDiag or (r-c) in negDiag:
                    continue

                board[r][c] = "Q"
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                
        backtrack(0)
        return res

