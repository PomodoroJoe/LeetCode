#------------------------------------------------------
# Solution 1 - while with for loops
#------------------------------------------------------

# Runtime:  14.71%
# Memory:   15.26%


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]

        min_row = 0
        min_col = 0

        max_row = n - 1
        max_col = n - 1

        max_count = n * n
        count = 0

        while count < max_count:
            # right
            for i in range(min_col, max_col + 1):
                count += 1
                result[min_row][i] = count
            min_row += 1

            # down
            for i in range(min_row, max_row + 1):
                count += 1
                result[i][max_col] = count
            max_col -= 1

            # left
            for i in range(max_col, min_col - 1, -1):
                count += 1
                result[max_row][i] = count
            max_row -= 1

            # up
            for i in range(max_row, min_row - 1, -1):
                count += 1
                result[i][min_col] = count
            min_col += 1

        return result