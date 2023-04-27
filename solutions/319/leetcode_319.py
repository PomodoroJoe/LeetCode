#------------------------------------------------------
# Solution 1 - math
#------------------------------------------------------

# Runtime:  62.63%
# Memory:   34.90%


class Solution:
    def bulbSwitch(self, n: int) -> int:
        from math import sqrt
        return int(sqrt(n))