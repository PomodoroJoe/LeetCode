#------------------------------------------------------
# Solution 1 - BFS
#------------------------------------------------------

# Runtime:  54.83%
# Memory:   41.32%


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_x = len(mat[0]) - 1
        max_y = len(mat) - 1

        result = [[-1] * (max_x + 1) for _ in range(max_y + 1)]

        queue = []

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if mat[y][x] == 0:
                    result[y][x] = 0
                    queue.append((x, y))

        
        while queue:
            cell = queue.pop(0)

            x, y = cell

            steps = result[y][x] + 1

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            directions = [up, dn, lt, rt]

            for d in directions:
                if not d:
                    continue

                next_x = d[0]
                next_y = d[1]

                if result[next_y][next_x] == -1 or result[next_y][next_x] > steps:
                    result[next_y][next_x] = steps
                    queue.append((next_x, next_y))

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ deque
#------------------------------------------------------

# Runtime:  89.90%
# Memory:   36.93%


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_x = len(mat[0]) - 1
        max_y = len(mat) - 1

        result = [[-1] * (max_x + 1) for _ in range(max_y + 1)]

        queue = deque([])

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if mat[y][x] == 0:
                    result[y][x] = 0
                    queue.append((x, y))

        
        while queue:
            cell = queue.popleft()

            x, y = cell

            steps = result[y][x] + 1

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            directions = [up, dn, lt, rt]

            for d in directions:
                if not d:
                    continue

                next_x, next_y = d

                if result[next_y][next_x] == -1 or result[next_y][next_x] > steps:
                    result[next_y][next_x] = steps
                    queue.append((next_x, next_y))

        return result


#------------------------------------------------------
# Solution 3 - Solution 2 w/o continue
#------------------------------------------------------

# Runtime:  90.81%
# Memory:   41.32%


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_x = len(mat[0]) - 1
        max_y = len(mat) - 1

        result = [[-1] * (max_x + 1) for _ in range(max_y + 1)]

        queue = deque([])

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if mat[y][x] == 0:
                    result[y][x] = 0
                    queue.append((x, y))

        
        while queue:
            cell = queue.popleft()

            x, y = cell

            steps = result[y][x] + 1

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            directions = [up, dn, lt, rt]

            for d in directions:
                if d:
                    next_x, next_y = d

                    if result[next_y][next_x] == -1 or result[next_y][next_x] > steps:
                        result[next_y][next_x] = steps
                        queue.append((next_x, next_y))

        return result