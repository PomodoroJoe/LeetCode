#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  98.96%
# Memory:   70.52%


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 == str2:
            return str1

        l1 = len(str1)
        l2 = len(str2)

        if l1 == l2:
            return ""

        result = ""

        if l1 > l2:
            remainder_str = str1[l2:]
            result = self.gcdOfStrings(str2, remainder_str)

        if l2 > l1:
            remainder_str = str2[l1:]
            result = self.gcdOfStrings(str1, remainder_str)

        # check result
        l3 = len(result)

        if l3 == 0:
            return ""

        m1 = l1 // l3
        if result * m1 != str1:
            return ""

        m2 = l2 // l3
        if result * m2 != str2:
            return ""

        return result



#------------------------------------------------------
# Solution 2 - recursive w/ symmetry check
#------------------------------------------------------

# Runtime:  81.48%
# Memory:   70.52%



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        if str1 == str2:
            return str1

        l1 = len(str1)
        l2 = len(str2)

        if l1 == l2:
            return ""

        result = ""

        if l1 > l2:
            remainder_str = str1[l2:]
            result = self.gcdOfStrings(str2, remainder_str)

        if l2 > l1:
            remainder_str = str2[l1:]
            result = self.gcdOfStrings(str1, remainder_str)

        return result



#------------------------------------------------------
# Solution 3 - math with custom gcd
#------------------------------------------------------

# Runtime:  75.26%
# Memory:   23.11%


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        if str1 == str2:
            return str1

        l1 = len(str1)
        l2 = len(str2)

        if l1 == l2:
            return ""

        result = ""

        def gcd(a, b):
            if a == 0:
                return b

            if b == 0:
                return a

            if a > b:
                r = a % b
                return gcd(b, r)

            r = b % a
            return gcd(a, r)

        l3 = gcd(l1, l2)
        if l3 == 0:
            return ""

        result = str1[:l3]
        return result



#------------------------------------------------------
# Solution 4 - math w/ python math.gcd
#------------------------------------------------------

# Runtime:  95.70%
# Memory:   70.52%


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        if str1 == str2:
            return str1

        l1 = len(str1)
        l2 = len(str2)

        if l1 == l2:
            return ""

        result = ""

        l3 = math.gcd(l1, l2)
        if l3 == 0:
            return ""

        result = str1[:l3]
        return result