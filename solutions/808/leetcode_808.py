#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def soupServings(self, n: int) -> float:

        def soupServingsRecurse(A, B, prob):
            if A == 0 and B > 0:
                return prob

            if A == 0 and B == 0:
                return 0.5 * prob

            if B == 0:
                return 0

            op1 = soupServingsRecurse(max(A - 100, 0), B, prob * 0.25)
            op2 = soupServingsRecurse(max(A - 75, 0), max(B - 25, 0), prob * 0.25)
            op3 = soupServingsRecurse(max(A - 50, 0), max(B - 50, 0), prob * 0.25)
            op4 = soupServingsRecurse(max(A - 25, 0), max(B - 75, 0), prob * 0.25)

            return op1 + op2 + op3 + op4

        result = soupServingsRecurse(n, n, 1.0)
        return result



#------------------------------------------------------
# Solution 3 - Solution 1 w/ cache
#------------------------------------------------------

# maximum recursion depth exceeded

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def soupServings(self, n: int) -> float:

        @cache
        def soupServingsRecurse(A, B):
            if A == 0 and B > 0:
                return 1.0

            if A == 0 and B == 0:
                return 0.5

            if B == 0:
                return 0

            op1 = soupServingsRecurse(max(A - 100, 0), B)
            op2 = soupServingsRecurse(max(A - 75, 0), max(B - 25, 0))
            op3 = soupServingsRecurse(max(A - 50, 0), max(B - 50, 0))
            op4 = soupServingsRecurse(max(A - 25, 0), max(B - 75, 0))

            return (op1 + op2 + op3 + op4) * 0.25

        result = soupServingsRecurse(n, n)
        return result



#------------------------------------------------------
# Solution 4 - Solution 3 w/ return multiplier
#------------------------------------------------------

# MEMORY EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def soupServings(self, n: int) -> float:

        @cache
        def soupServingsRecurse(A, B):
            if A == 0 and B > 0:
                return 1.0

            if A == 0 and B == 0:
                return 0.5

            if B == 0:
                return 0

            op1 = soupServingsRecurse(max(A - 100, 0), B)
            op2 = soupServingsRecurse(max(A - 75, 0), max(B - 25, 0))
            op3 = soupServingsRecurse(max(A - 50, 0), max(B - 50, 0))
            op4 = soupServingsRecurse(max(A - 25, 0), max(B - 75, 0))

            return (op1 + op2 + op3 + op4) * 0.25

        for x in range(25, n, 25):
            soupServingsRecurse(x, x)

        result = soupServingsRecurse(n, n)
        return result


#------------------------------------------------------
# Solution 5 - Solution 4 w/ pre-seed cache & early out
#------------------------------------------------------

# Runtime:  11.16%
# Memory:    6.51%


class Solution:
    def soupServings(self, n: int) -> float:

        @cache
        def soupServingsRecurse(A, B):
            if A == 0 and B > 0:
                return 1.0

            if A == 0 and B == 0:
                return 0.5

            if B == 0:
                return 0

            op1 = soupServingsRecurse(max(A - 100, 0), B)
            op2 = soupServingsRecurse(max(A - 75, 0), max(B - 25, 0))
            op3 = soupServingsRecurse(max(A - 50, 0), max(B - 50, 0))
            op4 = soupServingsRecurse(max(A - 25, 0), max(B - 75, 0))

            return (op1 + op2 + op3 + op4) * 0.25

        for x in range(25, n, 25):
            result = soupServingsRecurse(x, x)
            if result > (1 - 1e-5):
                return result


        result = soupServingsRecurse(n, n)
        return result


#------------------------------------------------------
# Solution 7 - Solution 5 w/ ml / 25
#------------------------------------------------------

# Runtime:  24.19%
# Memory:    6.51%


class Solution:
    def soupServings(self, n: int) -> float:

        @cache
        def soupServingsRecurse(A, B):
            if A <= 0 and B > 0:
                return 1.0

            if A <= 0 and B <= 0:
                return 0.5

            if B <= 0:
                return 0

            op1 = soupServingsRecurse(A - 4, B)
            op2 = soupServingsRecurse(A - 3, B - 1)
            op3 = soupServingsRecurse(A - 2, B - 2)
            op4 = soupServingsRecurse(A - 1, B - 3)

            return (op1 + op2 + op3 + op4) * 0.25

        new_n = ceil(n / 25)

        for x in range(1, new_n):
            result = soupServingsRecurse(x, x)
            if result > (1 - 1e-5):
                return result


        result = soupServingsRecurse(new_n, new_n)
        return result