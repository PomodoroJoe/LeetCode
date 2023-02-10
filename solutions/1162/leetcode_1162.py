#------------------------------------------------------
# Solution 1 - multipass (slow)
#------------------------------------------------------

# Runtime:  08.28%
# Memory:   91.37%



class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        result = -1

        working_grid = grid.copy()

        done = False
        while not done:
            done = True

            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    val = working_grid[y][x]

                    if val > 0:
                        up = (x, y - 1) if y > 0 else None
                        dn = (x, y + 1) if y < len(grid) - 1 else None
                        lt = (x - 1, y) if x > 0 else None
                        rt = (x + 1, y) if x < len(grid[0]) - 1 else None

                        coords = [up, dn, lt, rt]
                        for coord in coords:
                            if not coord:
                                continue

                            coord_x = coord[0]
                            coord_y = coord[1]

                            coord_val = working_grid[coord_y][coord_x]

                            if coord_val == 0 or coord_val > val + 1:
                                working_grid[coord_y][coord_x] = val + 1
                                done = False

        for row in working_grid:
            row_max = max(row)
            result = max(result, row_max)

        return result - 1 if result > 1 else -1