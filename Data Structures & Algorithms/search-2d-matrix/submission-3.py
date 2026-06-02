class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS =len(matrix), len(matrix[0])
        top, bottom=0, ROWS-1

        while top<=bottom:
            mid=(top+bottom)//2
            if target > matrix[mid][-1]:
                top=mid+1
            elif target < matrix[mid][0]:
                bottom=mid-1
            else:
                break

        if not (top<=bottom):
            return False


        left,right=0, COLS-1
        while left<=right:
            mid2=(left+right)//2
            if target > matrix[mid][mid2]:
                left=mid2+1
            elif target < matrix[mid][mid2]:
                right=mid2-1
            else:
                return True
        return False
