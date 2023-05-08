#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  32.44%
# Memory:    5.30%


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0

        max_col = len(mat[0]) - 1

        for row_num, row in enumerate(mat):
            primary = mat[row_num][row_num]
            secondary = mat[row_num][max_col - row_num]

            result += (primary + secondary) if row_num != max_col - row_num else primary

        return result