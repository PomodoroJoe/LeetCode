#------------------------------------------------------
# Solution 1 - BFS
#------------------------------------------------------

# Runtime:  97.98%
# Memory:   54.55%


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        result = 1

        n = len(grid)

        def firstLand():
            for y in range(n):
                for x in range(n):
                    if grid[y][x] == 1:
                        return (x, y)

        start = firstLand()
        visited = set()

        queue = [start]
        next_queue = []

        while queue:
            cell = queue.pop(0)

            visited.add(cell)

            x, y = cell
            
            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < n - 1 else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < n - 1 else None

            ops = [lt, rt, up, dn]

            for op in ops:
                if not op or op in visited:
                    continue

                next_x, next_y = op

                if grid[next_y][next_x] == 1:
                    queue.append(op)
                    visited.add(op)
                else:
                    next_queue.append((next_x, next_y, 1))

        queue = next_queue

        while queue:
            cell = queue.pop(0)

            visited.add(cell)

            x, y, b = cell
            
            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < n - 1 else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < n - 1 else None

            ops = [lt, rt, up, dn]

            for op in ops:
                if not op or op in visited:
                    continue

                next_x, next_y = op

                if grid[next_y][next_x] == 1:
                    return b
                else:
                    next_queue.append((next_x, next_y, b + 1))
                    visited.add(op)

        return result