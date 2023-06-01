#------------------------------------------------------
# Solution 1 - breadth first search w/ deque
#------------------------------------------------------

# Runtime:  53.97%
# Memory:   12.33%


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        target = (n - 1, n - 1)

        max_x = n - 1
        max_y = n - 1

        modifiers = [
            (-1,  1), (0,  1), (1,  1),
            (-1,  0),          (1,  0),
            (-1, -1), (0, -1), (1, -1)
        ]

        visited = set()

        queue = deque([(0, 0, 1)])

        while queue:
            x, y, steps = queue.popleft()

            if (x, y) == target:
                return steps

            for m in modifiers:
                next_x = x + m[0]
                next_y = y + m[1]

                if next_x < 0 or next_y < 0 or next_x > max_x or next_y > max_y:
                    continue

                if grid[next_y][next_x] == 1 or (next_x, next_y) in visited:
                    continue

                visited.add((next_x, next_y))

                queue.append((next_x, next_y, steps + 1))

        return -1