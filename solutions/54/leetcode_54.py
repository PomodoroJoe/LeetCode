#------------------------------------------------------
# Solution 1 - simple solution
#------------------------------------------------------

# Runtime:  12.57%
# Memory:    6.50%


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        row = 0
        col = 0

        min_row = 0
        max_row = len(matrix) - 1

        min_col = 0
        max_col = len(matrix[0]) - 1

        cell_count = (max_row + 1) * (max_col + 1)
        count = 0

        dcol = 1
        drow = 0

        while count < cell_count:
            result.append(matrix[row][col])
            count += 1

            row += drow
            col += dcol

            if col > max_col:
                drow = 1
                dcol = 0
                min_row += 1
                row = min_row
                col = max_col

            if row > max_row:
                drow = 0
                dcol = -1
                max_col -= 1
                row = max_row
                col = max_col

            if col < min_col:
                drow = -1
                dcol = 0
                max_row -= 1
                row = max_row
                col = min_col

            if row < min_row:
                drow = 0
                dcol = 1
                min_col += 1
                row = min_row
                col = min_col
                
        return result