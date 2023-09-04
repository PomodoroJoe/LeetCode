#------------------------------------------------------
# Solution 1 - full grid
#------------------------------------------------------

# Runtime:  30.35%
# Memory:   47.10%


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]

        grid[0][0] = 1

        for x in range(n):
            for y in range(m):
                if x == 0 and y == 0:
                    continue

                up = grid[y - 1][x] if y > 0 else 0
                lt = grid[y][x - 1] if x > 0 else 0
                grid[y][x] = up + lt

        return grid[m - 1][n - 1]



#------------------------------------------------------
# Solution 2 - prev row only
#------------------------------------------------------

# Runtime:  35.52%
# Memory:   47.10%


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row_above = [1] * n

        for y in range(1, m):
            current_row = [0] * n
            current_row[0] = 1

            for x in range(1, n):
                current_row[x] = current_row[x - 1] + row_above[x]

            row_above = current_row

        return row_above[-1]



#------------------------------------------------------
# Solution 3 - Solution 2 minified
#------------------------------------------------------

# Runtime:  90.87%
# Memory:   76.48%


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(1, m):
            next_row = [0] * n
            next_row[0] = 1

            for x in range(1, n):
                next_row[x] = next_row[x - 1] + row[x]
            row = next_row

        return row[-1]