#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        def minPathSumRecurse(x, y):

            if x == max_x and y == max_y:
                return grid[y][x]

            right = None
            if x < max_x:
                right = grid[y][x] + minPathSumRecurse(x+1, y)

            down = None
            if y < max_y:
                down = grid[y][x] + minPathSumRecurse(x, y+1)

            if right == None:
                return down

            if down == None:
                return right

            return min(right, down)

        return minPathSumRecurse(0, 0)



#------------------------------------------------------
# Solution 2 - recursive w/ dynamic programming
#------------------------------------------------------

# Runtime:  23.54%
# Memory:    8.47%


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        dp = {}

        def minPathSumRecurse(x, y):
            key = (x, y)
            if key in dp:
                return dp[key]

            if x == max_x and y == max_y:
                dp[key] = grid[y][x]
                return dp[key]

            right = None
            if x < max_x:
                right = grid[y][x] + minPathSumRecurse(x+1, y)

            down = None
            if y < max_y:
                down = grid[y][x] + minPathSumRecurse(x, y+1)

            if right == None:
                dp[key] = down
                return down

            if down == None:
                dp[key] = right
                return right

            dp[key] = min(right, down)
            return dp[key]

        return minPathSumRecurse(0, 0)



#------------------------------------------------------
# Solution 3 - recursive w/ cache
#------------------------------------------------------

# Runtime:  18.50%
# Memory:   11.37%


from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        @cache
        def minPathSumRecurse(x, y):
            if x == max_x and y == max_y:
                return grid[y][x]

            right = None
            if x < max_x:
                right = grid[y][x] + minPathSumRecurse(x+1, y)

            down = None
            if y < max_y:
                down = grid[y][x] + minPathSumRecurse(x, y+1)

            if right == None:
                return down

            if down == None:
                return right

            return min(right, down)

        return minPathSumRecurse(0, 0)



#------------------------------------------------------
# Solution 4 - recursive w/ dp & better min()
#------------------------------------------------------

# Runtime:  24.69%
# Memory:    8.47%


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        dp = {}

        def minPathSumRecurse(x, y):
            key = (x, y)
            if key in dp:
                return dp[key]

            if x == max_x and y == max_y:
                dp[key] = grid[y][x]
                return dp[key]

            right = None
            if x < max_x:
                right = grid[y][x] + minPathSumRecurse(x+1, y)

            down = None
            if y < max_y:
                down = grid[y][x] + minPathSumRecurse(x, y+1)

            if right == None:
                dp[key] = down
                return down

            if down == None:
                dp[key] = right
                return right

            dp[key] = right if right < down else down
            return dp[key]

        return minPathSumRecurse(0, 0)



#------------------------------------------------------
# Solution 5 - recursive w/ dp & better min() & inf
#------------------------------------------------------

# Runtime:  19.95%
# Memory:   11.37%


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        dp = {}

        def minPathSumRecurse(x, y):
            key = (x, y)
            if key in dp:
                return dp[key]

            if x == max_x and y == max_y:
                dp[key] = grid[y][x]
                return dp[key]

            right = inf
            if x < max_x:
                right = grid[y][x] + minPathSumRecurse(x+1, y)

            down = inf
            if y < max_y:
                down = grid[y][x] + minPathSumRecurse(x, y+1)

            dp[key] = right if right < down else down
            return dp[key]

        return minPathSumRecurse(0, 0)