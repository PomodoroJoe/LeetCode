#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# WROng ANSWER (test case t = 1)

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx - sx)
        dy = abs(fy - sy)

        steps = max(dx, dy)

        return steps <= t



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  47.88%
# Memory:   94.64%


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx - sx)
        dy = abs(fy - sy)

        steps = max(dx, dy)

        if t == 1:
            return steps == 1

        return steps <= t


#------------------------------------------------------
# Solution 3
#------------------------------------------------------

# Runtime:  70.90%
# Memory:   73.40%


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and sx == fx and sy == fy: return False

        dx = abs(fx - sx)
        dy = abs(fy - sy)
        
        steps = dx if dx > dy else dy
        return steps <= t