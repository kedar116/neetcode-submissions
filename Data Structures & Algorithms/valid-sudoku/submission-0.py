class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            s=set()
            for col in range(9):
                if board[row][col]==".":
                    continue 
                elif board[row][col] not in s:
                    s.add(board[row][col])
                else:
                    return False

        for col in range(9):
            s=set()
            for row in range(9):
                if board[row][col]==".":
                    continue
                elif board[row][col] not in s:
                    s.add(board[row][col])
                else:
                    return False
    
        for boxrow in range(0,9,3):
            for boxcol in range(0,9,3):
                s=set()
                for row in range(boxrow,boxrow+3):
                    for col in range(boxcol,boxcol+3):
                        if board[row][col]==".":
                            continue
                        elif board[row][col] not in s:
                            s.add(board[row][col])
                        else:
                            return False
        return True
        

            
