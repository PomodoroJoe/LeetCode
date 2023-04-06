#------------------------------------------------------
# Solution 1 - grid traversal with queue
#------------------------------------------------------

# Runtime:  35.47%
# Memory:   10.17%


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        visited = set()


        def isIsland(start_x, start_y):
            result = True

            queue = [(start_x, start_y)]

            while queue:
                coords = queue.pop(0)

                x = coords[0]
                y = coords[1]

                if grid[y][x] == 1:
                    continue

                if coords in visited:
                    continue

                visited.add(coords)

                if x == 0 or x == max_x or y == 0 or y == max_y:
                    result = False

                up = (x, y-1) if y > 0 else None
                dn = (x, y+1) if y < max_y else None
                lt = (x-1, y) if x > 0 else None
                rt = (x+1, y) if x < max_x else None

                directions = [up, dn, lt, rt]
                for d in directions:
                    if d != None:
                        queue.append(d)

            return result


        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if grid[y][x] == 1 or (x, y) in visited:
                    continue

                if isIsland(x, y):
                    result += 1

        return result


#------------------------------------------------------
# Solution 2 - grid traversal w/o continues
#------------------------------------------------------

# Runtime:  48.44%
# Memory:   14.25%


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        visited = set()

        def isIsland(start_x, start_y):
            result = True

            queue = [(start_x, start_y)]

            while queue:
                coords = queue.pop(0)

                x = coords[0]
                y = coords[1]

                if grid[y][x] == 0 and coords not in visited:

                    visited.add(coords)

                    if x == 0 or x == max_x or y == 0 or y == max_y:
                        result = False

                    up = (x, y-1) if y > 0 else None
                    dn = (x, y+1) if y < max_y else None
                    lt = (x-1, y) if x > 0 else None
                    rt = (x+1, y) if x < max_x else None

                    directions = [up, dn, lt, rt]
                    for d in directions:
                        if d != None:
                            queue.append(d)

            return result


        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if grid[y][x] == 0 and (x, y) not in visited:
                    if isIsland(x, y):
                        result += 1

        return result



#------------------------------------------------------
# Solution 3 - solution 2 but don't queue visited cells 
#------------------------------------------------------

# Runtime:  59.73%
# Memory:   14.25%


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        visited = set()

        def isIsland(start_x, start_y):
            result = True

            queue = [(start_x, start_y)]

            while queue:
                coords = queue.pop(0)

                x = coords[0]
                y = coords[1]

                if grid[y][x] == 0 and coords not in visited:

                    visited.add(coords)

                    if x == 0 or x == max_x or y == 0 or y == max_y:
                        result = False

                    up = (x, y-1) if y > 0 else None
                    dn = (x, y+1) if y < max_y else None
                    lt = (x-1, y) if x > 0 else None
                    rt = (x+1, y) if x < max_x else None

                    directions = [up, dn, lt, rt]
                    for d in directions:
                        if d and d not in visited:
                            queue.append(d)

            return result


        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if grid[y][x] == 0 and (x, y) not in visited:
                    if isIsland(x, y):
                        result += 1

        return result