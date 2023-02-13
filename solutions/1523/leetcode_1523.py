#------------------------------------------------------
# Solution 1 - math
#------------------------------------------------------

# Runtime:  23.50%
# Memory:   50.40%


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0

        num_count = high - low
        result = num_count // 2

        if low % 2 or high % 2:
            result += 1

        return result


#------------------------------------------------------
# Solution 2 - math (remove num_count)
#------------------------------------------------------

# Runtime:  23.50%
# Memory:   07.11%


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = (high - low) // 2

        if low % 2 or high % 2:
            result += 1

        return result


#------------------------------------------------------
# Solution 3 - math w/ optimizations
#------------------------------------------------------

# Runtime:  88.64%
# Memory:   07.11%


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 or high % 2:
            return 1 + (high - low) // 2

        return (high - low) // 2



#------------------------------------------------------
# Solution 4 - loop
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0

        for n in range(low, high + 1):
            if n % 2 == 1:
                result += 1

        return result


#------------------------------------------------------
# Solution 1 - loop w/ optimization
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0

        for n in range(low, high + 1):
            result += n % 2

        return result
