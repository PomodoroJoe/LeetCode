#------------------------------------------------------
# Solution 1 - BFS
#------------------------------------------------------

# Runtime:   5.40%
# Memory:   75.37%


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        result = 0

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        visited = set()

        def enclaveCount(start_x, start_y):
            count = 0

            isConnectedToBoundary = False

            queue = [(start_x, start_y)]

            while queue:
                x, y = queue.pop(0)

                if (x, y) in visited:
                    continue

                visited.add((x, y))

                if grid[y][x] == 0:
                    continue

                count += 1

                if x == 0 or x == max_x or y == 0 or y == max_y:
                    isConnectedToBoundary = True

                up = (x, y-1) if y > 0 else None
                dn = (x, y+1) if y < max_y else None
                lt = (x-1, y) if x > 0 else None
                rt = (x+1, y) if x < max_x else None

                options = [up, dn, lt, rt]

                for option in options:
                    if option != None:
                        queue.append((option[0], option[1]))

            return count if isConnectedToBoundary == False else 0
        

        for x in range(max_x + 1):
            for y in range(max_y + 1):

                if grid[y][x] == 1:
                    result += enclaveCount(x, y)

        return result



#------------------------------------------------------
# Solution 2 - BFS w/ input modification
#------------------------------------------------------

# Runtime:  14.92%
# Memory:   90.90%


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        result = 0

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        visited = grid

        def isVisited(x, y):
            return visited[y][x] == 0

        def visit(x, y):
            visited[y][x] = 0


        def enclaveCount(start_x, start_y):
            count = 0

            isConnectedToBoundary = False

            queue = [(start_x, start_y)]

            while queue:
                x, y = queue.pop(0)

                if isVisited(x, y):
                    continue

                visit(x, y)

                count += 1

                if x == 0 or x == max_x or y == 0 or y == max_y:
                    isConnectedToBoundary = True

                up = (x, y-1) if y > 0 else None
                dn = (x, y+1) if y < max_y else None
                lt = (x-1, y) if x > 0 else None
                rt = (x+1, y) if x < max_x else None

                options = [up, dn, lt, rt]

                for option in options:
                    if option != None:
                        queue.append((option[0], option[1]))

            return count if isConnectedToBoundary == False else 0
        

        for x in range(max_x + 1):
            for y in range(max_y + 1):

                if grid[y][x] == 1:
                    result += enclaveCount(x, y)

        return result



#------------------------------------------------------
# Solution 3 - BFS w/ input modification & better option
#------------------------------------------------------

# Runtime:  28.46%
# Memory:   90.90%


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        result = 0

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        visited = grid

        def enclaveCount(start_x, start_y):
            count = 0

            isConnectedToBoundary = False
            queue = [(start_x, start_y)]

            while queue:
                x, y = queue.pop(0)

                if visited[y][x] != 0:
                    visited[y][x] = 0
                    count += 1

                    if x == 0 or x == max_x or y == 0 or y == max_y:
                        isConnectedToBoundary = True

                    up = (x, y-1) if y > 0 else None
                    dn = (x, y+1) if y < max_y else None
                    lt = (x-1, y) if x > 0 else None
                    rt = (x+1, y) if x < max_x else None

                    options = [up, dn, lt, rt]

                    for option in options:
                        if option != None:
                            queue.append(option)

            return count if isConnectedToBoundary == False else 0
        
        for x in range(max_x + 1):
            for y in range(max_y + 1):

                if grid[y][x] == 1:
                    result += enclaveCount(x, y)

        return result