#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        max_x = len(pizza[0]) - 1
        max_y = len(pizza) - 1

        def hasApples(tl_x, tl_y, br_x, br_y):
            for j in range(tl_y, br_y+1):
                for i in range(tl_x, br_x+1):
                    if pizza[j][i] == 'A':
                        return True

            return False


        def waysRecurse(x, y, k):
            if k == 1:
                return 1 if hasApples(x, y, max_x, max_y) else 0

            result = 0

            # slice horizontally
            for j in range(y, max_y):
                if hasApples(x, y, max_x, j):
                    result += waysRecurse(x, j+1, k-1)

            # slice vertically
            for i in range(x, max_x):
                if hasApples(x, y, i, max_y):
                    result += waysRecurse(i+1, y, k-1)

            return result

        
        return waysRecurse(0, 0, k) % (pow(10, 9) + 7)



#------------------------------------------------------
# Solution 2 - recursive w/ cache
#------------------------------------------------------

# Runtime:  32.39%
# Memory:    5.10%


from functools import cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        max_x = len(pizza[0]) - 1
        max_y = len(pizza) - 1

        @cache
        def hasApples(tl_x, tl_y, br_x, br_y):
            for j in range(tl_y, br_y+1):
                for i in range(tl_x, br_x+1):
                    if pizza[j][i] == 'A':
                        return True

            return False


        @cache
        def waysRecurse(x, y, k):
            if k == 1:
                return 1 if hasApples(x, y, max_x, max_y) else 0

            result = 0

            # slice horizontally
            for j in range(y, max_y):
                if hasApples(x, y, max_x, j):
                    result += waysRecurse(x, j+1, k-1)

            # slice vertically
            for i in range(x, max_x):
                if hasApples(x, y, i, max_y):
                    result += waysRecurse(i+1, y, k-1)

            return result

        
        return waysRecurse(0, 0, k) % (pow(10, 9) + 7)



#------------------------------------------------------
# Solution 3 - recursive w/ cache & hasApplesCache
#------------------------------------------------------

# Runtime:  98.51%
# Memory:    9.80%


from functools import cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        max_x = len(pizza[0]) - 1
        max_y = len(pizza) - 1

        @cache
        def hasApples(tl_x, tl_y, br_x, br_y):
            for j in range(tl_y, br_y+1):
                for i in range(tl_x, br_x+1):
                    if pizza[j][i] == 'A':
                        return True

            return False


        @cache
        def waysRecurse(x, y, k):
            if k == 1:
                return 1 if hasApples(x, y, max_x, max_y) else 0

            result = 0

            # slice horizontally
            hasApplesCache = False
            for j in range(y, max_y):
                if hasApplesCache or hasApples(x, y, max_x, j):
                    hasApplesCache = True
                    result += waysRecurse(x, j+1, k-1)

            # slice vertically
            hasApplesCache = False
            for i in range(x, max_x):
                if hasApplesCache or hasApples(x, y, i, max_y):
                    hasApplesCache = True
                    result += waysRecurse(i+1, y, k-1)

            return result

        
        return waysRecurse(0, 0, k) % (pow(10, 9) + 7)
