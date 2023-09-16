#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  24.20%
# Memory:   81.49%


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        max_x = len(heights[0]) - 1
        max_y = len(heights) - 1

        efforts = [[inf] * (max_x + 1) for _ in range(max_y + 1)]

        queue = [(0, 0)]
        efforts[0][0] = 0

        while queue:
            cell = queue.pop(0)

            x, y = cell

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            directions = [up, dn, lt, rt]

            height = heights[y][x]
            effort = efforts[y][x]

            for d in directions:
                if d == None:
                    continue
                
                dx, dy = d
                next_effort = abs(height - heights[dy][dx])
                next_effort = max(next_effort, effort)

                if next_effort < efforts[dy][dx]:
                    efforts[dy][dx] = next_effort
                    queue.append(d)

        return efforts[max_y][max_x]


#------------------------------------------------------
# Solution 3 - Solution 1 w/ deque and custom max
#------------------------------------------------------

# Runtime:  27.67%
# Memory:   98.23%


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        max_x = len(heights[0]) - 1
        max_y = len(heights) - 1

        efforts = [[inf] * (max_x + 1) for _ in range(max_y + 1)]

        queue = deque([(0, 0)])
        efforts[0][0] = 0

        while queue:
            cell = queue.popleft()

            x, y = cell

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            directions = [up, dn, lt, rt]

            height = heights[y][x]
            effort = efforts[y][x]

            for d in directions:
                if d == None:
                    continue
                
                dx, dy = d
                next_effort = abs(height - heights[dy][dx])
                next_effort = next_effort if next_effort > effort else effort

                if next_effort < efforts[dy][dx]:
                    efforts[dy][dx] = next_effort
                    queue.append(d)

        return efforts[max_y][max_x]