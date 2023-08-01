#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  33.18%
# Memory:   13.43%


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @cache
        def minimumDeleteSumRecurse(i1, i2):
            if i1 >= len(s1) and i2 >= len(s2):
                return 0

            if i1 >= len(s1):
                result = 0
                while i2 < len(s2):
                    result += ord(s2[i2])
                    i2 += 1
                return result

            if i2 >= len(s2):
                result = 0
                while i1 < len(s1):
                    result += ord(s1[i1])
                    i1 += 1
                return result

            if s1[i1] == s2[i2]:
                return minimumDeleteSumRecurse(i1 + 1, i2 + 1)

            option1 = ord(s1[i1]) + minimumDeleteSumRecurse(i1 + 1, i2)
            option2 = ord(s2[i2]) + minimumDeleteSumRecurse(i1, i2 + 1)

            return min(option1, option2)

        
        return minimumDeleteSumRecurse(0, 0)