#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 1:
            return 1

        def isPalendrome(p):
            return p == p[::-1]

        if isPalendrome(s):
            return len(s)

        result = 0
        for i in range(len(s)):
            left = s[:i]
            right = s[i+1:]

            new_s = left + right
            option = self.longestPalindromeSubseq(new_s)

            result = max(result, option)

        return result



#------------------------------------------------------
# Solution 2 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


from functools import cache

class Solution:

    @cache
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 1:
            return 1

        def isPalendrome(p):
            return p == p[::-1]

        if isPalendrome(s):
            return len(s)

        result = 0
        for i in range(len(s)):
            left = s[:i]
            right = s[i+1:]

            new_s = left + right
            option = self.longestPalindromeSubseq(new_s)

            result = max(result, option)

        return result



#------------------------------------------------------
# Solution 3 - recursive w/ left & right index
#------------------------------------------------------

# Runtime:  87.26%
# Memory:    6.26%


from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def palendromeLen(left, right):
            if left > right:
                return 0

            if left == right:
                return 1

            if s[left] == s[right]:
                return 2 + palendromeLen(left+1, right-1)

            option_1 = palendromeLen(left+1, right)
            option_2 = palendromeLen(left, right-1)

            return max(option_1, option_2)

        return palendromeLen(0, len(s) - 1)



#------------------------------------------------------
# Solution 4 - Solution 3 w/ custom max()
#------------------------------------------------------

# Runtime:  97.50%
# Memory:   11.13%


from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def palendromeLen(left, right):
            if left > right:
                return 0

            if left == right:
                return 1

            if s[left] == s[right]:
                return 2 + palendromeLen(left+1, right-1)

            option_1 = palendromeLen(left+1, right)
            option_2 = palendromeLen(left, right-1)

            return option_1 if option_1 > option_2 else option_2

        return palendromeLen(0, len(s) - 1)