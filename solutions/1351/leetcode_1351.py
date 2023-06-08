#------------------------------------------------------
# Solution 1 - exhaustive search
#------------------------------------------------------

# Runtime:  14.35%
# Memory:   66.13%


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    result += 1

        return result



#------------------------------------------------------
# Solution 2 - breadth first search
#------------------------------------------------------

# Runtime:  75.89%
# Memory:   14.16%


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        max_x = n - 1
        max_y = m - 1

        total = m * n
        non_negative = 0

        queue = [(0, 0)]
        visited = set((0, 0))

        while queue:
            x, y = queue.pop(0)

            if grid[y][x] >= 0:
                non_negative += 1

                right = (x + 1, y) if x < max_x else None
                down  = (x, y + 1) if y < max_y else None

                if right and right not in visited:
                    visited.add(right)
                    queue.append(right)

                if down and down not in visited:
                    visited.add(down)
                    queue.append(down)

        return total - non_negative