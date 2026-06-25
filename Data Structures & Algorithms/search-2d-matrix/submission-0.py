class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # we need to search a 2 D matrix.
        # If we observe we understand that the matrix is in a sorted format.
        # we first need to find the optimum row and then we perform binary search on the optimum row.

        ROWS=len(matrix)
        COLS=len(matrix[0])


        top=0
        bottom=ROWS-1


        while top<=bottom:
            row=(top+bottom)//2
            # if the target is greater than the greatest elemnet of this row, then we change rows
            if target>matrix[row][-1]:
                #we move upwards
                top=row+1
            # if the target is smalller than the smallest element in the current row
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                # we have found the row
                break
            

        # the current row value is the correct row

        left=0
        right=len(matrix[0])-1

        while left<=right:
            mid=(left+right)//2

            if matrix[row][mid]>target:
                right=mid-1
            elif matrix[row][mid]<target:
                left=mid+1
            else:
                return True
        return False

