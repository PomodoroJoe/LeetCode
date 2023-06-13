#------------------------------------------------------
# Solution 1 - two loops
#------------------------------------------------------

# Runtime:  45.60%
# Memory:   74.87%


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0

        # key = row, value = count
        rows = defaultdict(int)

        # key = col, value = count
        cols = defaultdict(int)

        n = len(grid)

        for i in range(n):
            row = grid[i]
            rows[tuple(row)] += 1

            col = []
            for j in range(n):
                val = grid[j][i]
                col.append(val)

            cols[tuple(col)] += 1

        for key in rows:
            if key in cols:
                result += rows[key] * cols[key]

        return result



#------------------------------------------------------
# Solution 2 - zip
#------------------------------------------------------

# Runtime:  76.73%
# Memory:   26.88%


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0

        rows = defaultdict(int)
        cols = defaultdict(int)

        n = len(grid)

        for row in grid:
            rows[tuple(row)] += 1

        rotated_grid = list(zip(*grid))

        for col in rotated_grid:
            cols[tuple(col)] += 1

        for key in rows:
            if key in cols:
                result += rows[key] * cols[key]

        return result



#------------------------------------------------------
# Solution 3 - Solution 2 (optimized)
#------------------------------------------------------

# Runtime:  94.85%
# Memory:   41.90%


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        rotated_grid = list(zip(*grid))

        cols = defaultdict(int)
        for col in rotated_grid:
            cols[col] += 1

        result = 0
        for key in rows:
            result += rows[key] * cols[key]

        return result