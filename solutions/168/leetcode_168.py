#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  88.27%
# Memory:   23.11%


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        col = columnNumber

        while col > 0:
            index = (col - 1) % 26
            col = (col - 1) // 26

            result = mapping[index] + result

        return result



#------------------------------------------------------
# Solution 4 - minified
#------------------------------------------------------

# Runtime:  78.61%
# Memory:   89.71%


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        c = columnNumber

        while c > 0:
            c -= 1
            i = c % 26
            c = c // 26
            r = m[i] + r
        return r


#------------------------------------------------------
# Solution 6 - ord & chr
#------------------------------------------------------

# Runtime:  71.85%
# Memory:   89.71%


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = ""
        c = columnNumber

        b = ord('A')

        while c > 0:
            i = (c - 1) % 26
            c = (c - 1) // 26

            r = chr(b + i) + r

        return r