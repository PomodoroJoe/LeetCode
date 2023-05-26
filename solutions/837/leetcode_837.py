#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


from functools import cache

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        result = 0

        if k == 0:
            return 1.0

        per_draw_probabiltiy = 1.0 / maxPts

        @cache
        def probabiltiy_of_points(p):
            if p == 0:
                return 1.0

            probability = 0

            min_index = p - maxPts if p > maxPts else 0
            max_index = min(p, k)

            for index in range(min_index, max_index):
                probability += probabiltiy_of_points(index) * per_draw_probabiltiy

            return probability


        for p in range(k, n+1):
            result += probabiltiy_of_points(p)

        return result



#------------------------------------------------------
# Solution 2 - iterative
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        result = 0

        if k == 0:
            return 1.0

        per_draw_probabiltiy = 1.0 / maxPts

        probabiltiy_of_points = [0] * (n + 1)
        probabiltiy_of_points[0] = 1.0

        for p in range(1, n + 1):
            min_index = p - maxPts if p > maxPts else 0
            max_index = min(p, k)
            
            probability = sum(probabiltiy_of_points[min_index:max_index]) * per_draw_probabiltiy
            probabiltiy_of_points[p] = probability


        for p in range(k, n+1):
            result += probabiltiy_of_points[p]

        return result



#------------------------------------------------------
# Solution 3 - Solution 2 w/ running sum
#------------------------------------------------------

# Runtime:   7.65%
# Memory:   52.39%


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        result = 0

        if k == 0 or n >= (k + maxPts):
            return 1.0

        per_draw_probabiltiy = 1.0 / maxPts

        probabiltiy_of_points = [0] * (n + 1)
        probabiltiy_of_points[0] = 1.0

        running_sum = 0

        for p in range(1, n + 1):
            min_index = p - maxPts if p > maxPts else 0
            max_index = min(p, k)

            # sum(probabiltiy_of_points[min_index:max_index])
            running_sum -= probabiltiy_of_points[min_index - 1] if min_index > 0 else 0
            running_sum += probabiltiy_of_points[max_index - 1] if p <= k else 0
            
            probability = running_sum * per_draw_probabiltiy
            probabiltiy_of_points[p] = probability


        for p in range(k, n+1):
            result += probabiltiy_of_points[p]

        return result