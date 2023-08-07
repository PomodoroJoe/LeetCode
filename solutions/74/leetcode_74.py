#------------------------------------------------------
# Solution 1 - recursive binary search
#------------------------------------------------------

# Runtime:  80.47%
# Memory:   64.57%


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_count = len(matrix)
        col_count = len(matrix[0])


        def index_to_coord(index):
            row = index // col_count
            col = index % col_count
            return (row, col)

        def searchMatrixRecurse(low_index, high_index):
            if low_index >= high_index:
                return False

            mid_index = low_index + ((high_index - low_index) // 2)

            coord = index_to_coord(mid_index)

            val = matrix[coord[0]][coord[1]]
            if val == target:
                return True

            if val < target:
                return searchMatrixRecurse(mid_index + 1, high_index)
            else:
                return searchMatrixRecurse(low_index, mid_index)

        return searchMatrixRecurse(0, row_count * col_count)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ fast mid index calc
#------------------------------------------------------

# Runtime:  90.75%
# Memory:   28.37%


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_count = len(matrix)
        col_count = len(matrix[0])


        def index_to_coord(index):
            row = index // col_count
            col = index % col_count
            return (row, col)

        def searchMatrixRecurse(low_index, high_index):
            if low_index >= high_index:
                return False

            mid_index = (high_index + low_index) // 2
            coord = index_to_coord(mid_index)

            val = matrix[coord[0]][coord[1]]
            if val == target:
                return True

            if val < target:
                return searchMatrixRecurse(mid_index + 1, high_index)
            else:
                return searchMatrixRecurse(low_index, mid_index)

        return searchMatrixRecurse(0, row_count * col_count)