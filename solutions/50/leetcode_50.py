#------------------------------------------------------
# Solution 1 - internal function
#------------------------------------------------------

# Runtime:  67.85%
# Memory:   41.10%


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)



#------------------------------------------------------
# Solution 2 - internal function 2
#------------------------------------------------------

# Runtime:  26.00%
# Memory:   19.50%


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


#------------------------------------------------------
# Solution 3 - for loop
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n == 1:
            return x

        result = 1

        if n < 0:
            n = -n
            x = 1 / x

        for _ in range(n):
            result = result * x

        return result


#------------------------------------------------------
# Solution 4 - recursive
#------------------------------------------------------

# Runtime:  83.46%
# Memory:    7.14%


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n == 1:
            return x

        if n < 0:
            n = -n
            x = 1 / x

        result = self.myPow(x, n // 2)
        result = result * result

        if n % 2:
            result = result * x

        return result


#------------------------------------------------------
# Solution 5 - Solution 4 w/ cache
#------------------------------------------------------

# Runtime:  26.00%
# Memory:    7.14%


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n == 1:
            return x

        if n < 0:
            n = -n
            x = 1 / x

        result = self.myPow(x, n // 2)
        result = result * result

        if n % 2:
            result = result * x

        return result


#------------------------------------------------------
# Solution 6 - Solution 4 (minified-ish)
#------------------------------------------------------

# Runtime:  99.40%
# Memory:   41.10%


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x

        if n < 0:
            x = 1 / x
            n = -n

        result = self.myPow(x, n // 2)
        result = result * result

        if n % 2:
            result = result * x

        return result