#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3

        if not s2:
            return s1 == s3

        if not s3:
            return False

        option_1 = False
        if s1[0] == s3[0]:
            option_1 = self.isInterleave(s1[1:], s2, s3[1:])

        option_2 = False
        if s2[0] == s3[0]:
            option_2 = self.isInterleave(s1, s2[1:], s3[1:])

        return option_1 or option_2


#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  86.82%
# Memory:    5.90%


class Solution:

    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3

        if not s2:
            return s1 == s3

        if not s3:
            return False

        option_1 = False
        if s1[0] == s3[0]:
            option_1 = self.isInterleave(s1[1:], s2, s3[1:])

        option_2 = False
        if s2[0] == s3[0]:
            option_2 = self.isInterleave(s1, s2[1:], s3[1:])

        return option_1 or option_2



#------------------------------------------------------
# Solution 3 - recursive with index
#------------------------------------------------------

# Runtime:  67.25%
# Memory:   15.80%


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        max_i1 = len(s1) - 1
        max_i2 = len(s2) - 1
        max_i3 = len(s3) - 1

        @cache
        def isInterleaveRecurse(i1, i2, i3):
            if i1 > max_i1:
                return s2[i2:] == s3[i3:]

            if i2 > max_i2:
                return s1[i1:] == s3[i3:]

            if i3 > max_i3:
                return False

            option_1 = False
            if s1[i1] == s3[i3]:
                option_1 = isInterleaveRecurse(i1 + 1, i2, i3 + 1)

            option_2 = False
            if s2[i2] == s3[i3]:
                option_2 = isInterleaveRecurse(i1, i2 + 1, i3 + 1)

            return option_1 or option_2

        return isInterleaveRecurse(0, 0, 0)


#------------------------------------------------------
# Solution 4 - Solution 3 w/o cache (custom memo)
#------------------------------------------------------

# Runtime:  52.60%
# Memory:   19.84%


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        max_i1 = len(s1) - 1
        max_i2 = len(s2) - 1
        max_i3 = len(s3) - 1

        memo = {}

        def isInterleaveRecurse(i1, i2, i3):
            key = (i1, i2, i3)
            if key in memo:
                return memo[key]

            if i1 > max_i1:
                memo[key] = s2[i2:] == s3[i3:]
                return memo[key]

            if i2 > max_i2:
                memo[key] = s1[i1:] == s3[i3:]
                return memo[key]

            if i3 > max_i3:
                memo[key] = False
                return False

            option_1 = False
            if s1[i1] == s3[i3]:
                option_1 = isInterleaveRecurse(i1 + 1, i2, i3 + 1)

            option_2 = False
            if s2[i2] == s3[i3]:
                option_2 = isInterleaveRecurse(i1, i2 + 1, i3 + 1)

            memo[key] = option_1 or option_2
            return memo[key]

        return isInterleaveRecurse(0, 0, 0)