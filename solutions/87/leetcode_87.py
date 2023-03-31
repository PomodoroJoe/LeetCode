#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def isScrambleRecurse(x1, x2):
            
            if len(x1) == 1 and x1 == x2:
                return True

            if sorted(x1) != sorted(x2):
                return False

            for i in range(1, len(x1)):
                left_1 = x1[:i]
                right_1 = x1[i:]

                left_2 = x2[:i]
                right_2 = x2[i:]

                left_3 = x2[::-1][:i]
                right_3 = x2[::-1][i:]

                if isScrambleRecurse(left_1, left_2) and isScrambleRecurse(right_1, right_2):
                    return True

                if isScrambleRecurse(left_1, left_3) and isScrambleRecurse(right_1, right_3):
                    return True

            return False

        return isScrambleRecurse(s1, s2)



#------------------------------------------------------
# Solution 2 - recursive w/ cache
#------------------------------------------------------

# Runtime:  70.93%
# Memory:   42.97%


from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @cache
        def isScrambleRecurse(x1, x2):
            
            if len(x1) == 1 and x1 == x2:
                return True

            if sorted(x1) != sorted(x2):
                return False

            for i in range(1, len(x1)):
                left_1 = x1[:i]
                right_1 = x1[i:]

                left_2 = x2[:i]
                right_2 = x2[i:]

                left_3 = x2[::-1][:i]
                right_3 = x2[::-1][i:]

                if isScrambleRecurse(left_1, left_2) and isScrambleRecurse(right_1, right_2):
                    return True

                if isScrambleRecurse(left_1, left_3) and isScrambleRecurse(right_1, right_3):
                    return True

            return False

        return isScrambleRecurse(s1, s2)