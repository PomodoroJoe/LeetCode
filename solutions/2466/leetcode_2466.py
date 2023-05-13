#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:


        def countGoodStringsRecurse(length):
            if length > high:
                return 0

            result = 1 if length >= low else 0

            result += countGoodStringsRecurse(length + zero)
            result += countGoodStringsRecurse(length + one)

            return result % (pow(10, 9) + 7)

        return countGoodStringsRecurse(0)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  39.55%
# Memory:   36.57%


from functools import cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        @cache
        def countGoodStringsRecurse(length):
            if length > high:
                return 0

            result = 1 if length >= low else 0

            result += countGoodStringsRecurse(length + zero)
            result += countGoodStringsRecurse(length + one)

            return result % (pow(10, 9) + 7)

        return countGoodStringsRecurse(0)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ negative indexes
#------------------------------------------------------

# Runtime:  57.46%
# Memory:   36.57%


rom functools import cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        mod_val = (pow(10, 9) + 7)

        @cache
        def countGoodStringsRecurse(length):
            if length > high:
                return 0

            result = 1 if length >= low else 0

            result += countGoodStringsRecurse(length + zero)
            result += countGoodStringsRecurse(length + one)

            return result % mod_val

        return countGoodStringsRecurse(0)



#------------------------------------------------------
# Solution 4 - iterative
#------------------------------------------------------

# Runtime:  23.88%
# Memory:   11.19%


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod_val = (pow(10, 9) + 7)

        # index = string length
        results = [1] + [0] * high

        for i in range(1, high + 1):
            results[i] += results[i - zero] if i >= zero else 0
            results[i] += results[i - one] if i >= one else 0

        return sum(results[low:high + 1]) % mod_val



#------------------------------------------------------
# Solution 5 - Solution 4 w/ simplified result
#------------------------------------------------------

# Runtime:  29.10%
# Memory:   11.19%


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod_val = (pow(10, 9) + 7)

        # index = string length
        results = [1] + [0] * high

        for i in range(1, high + 1):
            results[i] += results[i - zero] + results[i - one]

        return sum(results[low:high + 1]) % mod_val



#------------------------------------------------------
# Solution 6 - Solution 5 w/ early mods
#------------------------------------------------------

# Runtime:  97.76%
# Memory:   66.42%


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod_val = (pow(10, 9) + 7)

        # index = string length
        results = [1] + [0] * high

        for i in range(1, high + 1):
            results[i] += (results[i - zero] + results[i - one]) % mod_val

        return sum(results[low:high + 1]) % mod_val



#------------------------------------------------------
# Solution 7 - Solution 6 w/o whitespace
#------------------------------------------------------

# Runtime:  97.76%
# Memory:   71.64%


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod_val = (pow(10, 9) + 7)
        results = [1] + [0] * high
        for i in range(1, high + 1):
            results[i] += (results[i - zero] + results[i - one]) % mod_val
        return sum(results[low:high + 1]) % mod_val