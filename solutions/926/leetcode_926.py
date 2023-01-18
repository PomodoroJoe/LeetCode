#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  97.71%
# Memory:   72.55%

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        result = 0
        ones_count = 0

        for c in s:
            if c == "0":
                if ones_count > 0:
                    result += 1
                    ones_count -= 1
            else:
                ones_count += 1

        return result
