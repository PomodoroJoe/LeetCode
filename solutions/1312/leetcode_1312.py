#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  82.60%
# Memory:   19.50%


class Solution:
    def minInsertions(self, s: str) -> int:
        def minInsertionsRecurse(left, right):
            if left >= right:
                return 0

            if s[left] == s[right]:
                return minInsertionsRecurse(left + 1, right - 1)

            option_1 = 1 + minInsertionsRecurse(left, right - 1)
            option_2 = 1 + minInsertionsRecurse(left + 1, right)

            return min(option_1, option_2)
                
        return minInsertionsRecurse(0, len(s) - 1)


#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  61.65%
# Memory:   14.41%


from functools import cache

class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def minInsertionsRecurse(left, right):
            if left >= right:
                return 0

            if s[left] == s[right]:
                return minInsertionsRecurse(left + 1, right - 1)

            option_1 = 1 + minInsertionsRecurse(left, right - 1)
            option_2 = 1 + minInsertionsRecurse(left + 1, right)

            return min(option_1, option_2)
                
        return minInsertionsRecurse(0, len(s) - 1)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ custom min()
#------------------------------------------------------

# Runtime:  70.34%
# Memory:   14.83%


from functools import cache

class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def minInsertionsRecurse(left, right):
            if left >= right:
                return 0

            if s[left] == s[right]:
                return minInsertionsRecurse(left + 1, right - 1)

            option_1 = 1 + minInsertionsRecurse(left, right - 1)
            option_2 = 1 + minInsertionsRecurse(left + 1, right)

            return option_1 if option_1 < option_2 else option_2
                
        return minInsertionsRecurse(0, len(s) - 1)



#------------------------------------------------------
# Solution 7 - Solution 2 (minimized)
#------------------------------------------------------

# Runtime:  72.67%
# Memory:   14.62%


from functools import cache

class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def minInsertionsRecurse(l, r):
            if l >= r: return 0
            if s[l] == s[r]: return minInsertionsRecurse(l + 1, r - 1)

            op_1 = 1 + minInsertionsRecurse(l, r - 1)
            op_2 = 1 + minInsertionsRecurse(l + 1, r)

            return op_1 if op_1 < op_2 else op_2
                
        return minInsertionsRecurse(0, len(s) - 1)