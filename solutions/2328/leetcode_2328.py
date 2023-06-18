#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  94.71%
# Memory:   54.33%


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        result = 0
    
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        mod_val = 10**9 + 7

        working_grid = [[0] * len(grid[0]) for _ in grid]


        def cellPaths(x, y):
            if working_grid[y][x] > 0:
                return working_grid[y][x]

            val = grid[y][x]

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            cells = [up, dn, lt, rt]

            path_count = 1

            for cell in cells:
                if not cell: continue
                cx, cy = cell

                if grid[cy][cx] < val:
                    path_count += cellPaths(cx, cy)

            working_grid[y][x] = path_count
            return path_count


        for x in range(max_x + 1):
            for y in range(max_y + 1):
                result += cellPaths(x, y)

        return result % mod_val



#------------------------------------------------------
# Solution 2 - Solution 1 w/ early mod
#------------------------------------------------------

# Runtime:  94.71%
# Memory:   79.33%


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        result = 0
    
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        mod_val = 10**9 + 7

        working_grid = [[0] * len(grid[0]) for _ in grid]


        def cellPaths(x, y):
            if working_grid[y][x] > 0:
                return working_grid[y][x]

            val = grid[y][x]

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            cells = [up, dn, lt, rt]

            path_count = 1

            for cell in cells:
                if not cell: continue
                cx, cy = cell

                if grid[cy][cx] < val:
                    path_count += cellPaths(cx, cy)

            working_grid[y][x] = path_count % mod_val
            return path_count


        for x in range(max_x + 1):
            for y in range(max_y + 1):
                result += cellPaths(x, y)

        return result % mod_val