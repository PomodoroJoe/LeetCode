#------------------------------------------------------
# Solution 1 - recursive w/ dp
#------------------------------------------------------

# Runtime:  83.69%
# Memory:    7.12%


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        max_x = len(obstacleGrid[0]) - 1
        max_y = len(obstacleGrid) - 1 

        dp = {}

        def uniquePathsWithObstaclesRecurse(x, y):
            key = (x, y)
            if key in dp:
                return dp[key]

            if obstacleGrid[y][x] == 1:
                dp[key] = 0
                return 0

            if x == 0 and y == 0:
                dp[key] = 1
                return 1

            if x < 0:
                dp[key] = 0
                return 0

            if y < 0:
                dp[key] = 0
                return 0

            up = uniquePathsWithObstaclesRecurse(x, y - 1)
            lt = uniquePathsWithObstaclesRecurse(x - 1, y)

            dp[key] = up + lt
            return dp[key]

        return uniquePathsWithObstaclesRecurse(max_x, max_y)


#------------------------------------------------------
# Solution 2 - Solution 1 w/ @cache
#------------------------------------------------------

# Runtime:  33.92%
# Memory:   14.80%


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        max_x = len(obstacleGrid[0]) - 1
        max_y = len(obstacleGrid) - 1 

        @cache
        def uniquePathsWithObstaclesRecurse(x, y):
            if obstacleGrid[y][x] == 1:
                return 0

            if x == 0 and y == 0:
                return 1

            if x < 0:
                return 0

            if y < 0:
                return 0

            up = uniquePathsWithObstaclesRecurse(x, y - 1)
            lt = uniquePathsWithObstaclesRecurse(x - 1, y)

            return up + lt

        return uniquePathsWithObstaclesRecurse(max_x, max_y)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ better base cases
#------------------------------------------------------

# Runtime:  95.20%
# Memory:    7.12%


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        max_x = len(obstacleGrid[0]) - 1
        max_y = len(obstacleGrid) - 1 

        @cache
        def uniquePathsWithObstaclesRecurse(x, y):
            if obstacleGrid[y][x] == 1:
                return 0

            if x == 0 and y == 0:
                return 1

            if x < 0 or y < 0:
                return 0

            up = uniquePathsWithObstaclesRecurse(x, y - 1)
            lt = uniquePathsWithObstaclesRecurse(x - 1, y)

            return up + lt

        return uniquePathsWithObstaclesRecurse(max_x, max_y)



#------------------------------------------------------
# Solution 4 - iterative
#------------------------------------------------------

# Runtime:  69.70%
# Memory:   97.55%


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        x_count = len(obstacleGrid[0])
        y_count = len(obstacleGrid)

        answer_grid = [[0] * x_count for _ in range(y_count)]
        answer_grid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for y in range(y_count):
            for x in range(x_count):
                if obstacleGrid[y][x] == 1:
                    continue

                if y > 0:
                    answer_grid[y][x] += answer_grid[y - 1][x]

                if x > 0:
                    answer_grid[y][x] += answer_grid[y][x - 1]

        return answer_grid[y_count - 1][x_count - 1]