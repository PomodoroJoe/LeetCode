#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def tribonacci(self, n: int) -> int:
        # base case(s)
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        # recursive case(s)
        # (reducing problem)

        n_1 = self.tribonacci(n - 1)
        n_2 = self.tribonacci(n - 2)
        n_3 = self.tribonacci(n - 3)

        return n_1 + n_2 + n_3



#------------------------------------------------------
# Solution 2 - recursive w/ @cache
#------------------------------------------------------

# Runtime:  76.15%
# Memory:   53.98%


from functools import cache

class Solution:

    @cache
    def tribonacci(self, n: int) -> int:
        # base case(s)
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        # recursive case(s)
        # (reducing problem)

        n_1 = self.tribonacci(n - 1)
        n_2 = self.tribonacci(n - 2)
        n_3 = self.tribonacci(n - 3)

        return n_1 + n_2 + n_3



#------------------------------------------------------
# Solution 3 - recursive w/ dynamic programming
#------------------------------------------------------

# Runtime:  80.17%
# Memory:   53.98%


class Solution:

    dp = {}

    def tribonacci(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]

        # base case(s)
        if n == 0:
            self.dp[n] = 0
            return 0

        if n == 1:
            self.dp[n] = 1
            return 1

        if n == 2:
            self.dp[n] = 1
            return 1

        # recursive case(s)
        # (reducing problem)

        n_1 = self.tribonacci(n - 1)
        n_2 = self.tribonacci(n - 2)
        n_3 = self.tribonacci(n - 3)

        self.dp[n] = n_1 + n_2 + n_3
        return self.dp[n]



#------------------------------------------------------
# Solution 4 - recursive w/ dynamic programming seeded
#------------------------------------------------------

# Runtime:  76.15%
# Memory:   10.15%


class Solution:

    dp = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]

        n_1 = self.tribonacci(n - 1)
        n_2 = self.tribonacci(n - 2)
        n_3 = self.tribonacci(n - 3)

        self.dp[n] = n_1 + n_2 + n_3
        return self.dp[n]



#------------------------------------------------------
# Solution 5 - iterative
#------------------------------------------------------

# Runtime:  90.49%
# Memory:   53.98%


class Solution:
    def tribonacci(self, n: int) -> int:
        tribs = [0, 1, 1]

        index = 3
        while index <= n:
            tribs.append(tribs[index - 1] + tribs[index - 2] + tribs[index - 3])
            index += 1

        return tribs[n]
