#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  18.00%
# Memory:   39.79%


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        current_num = num
        next_num = 0

        while current_num:
            next_num += current_num % 10
            current_num = current_num // 10

        return self.addDigits(next_num)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ @cache
#------------------------------------------------------

# Runtime:   6.65%
# Memory:   39.79%


from functools import cache

class Solution:

    @cache    
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        current_num = num
        next_num = 0

        while current_num:
            next_num += current_num % 10
            current_num = current_num // 10

        return self.addDigits(next_num)




#------------------------------------------------------
# Solution 3 - Solution 1 w/ early return
#------------------------------------------------------

# Runtime:  84.34%
# Memory:   39.79%


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        current_num = num
        next_num = 0

        while current_num:
            next_num += current_num % 10
            current_num = current_num // 10

        return self.addDigits(next_num) if next_num >= 10 else next_num




#------------------------------------------------------
# Solution 4 - Solution 3 w/ string
#------------------------------------------------------

# Runtime:  98.73%
# Memory:   39.79%


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        current_num = str(num)
        next_num = 0

        for c in current_num:
            next_num += int(c)

        return self.addDigits(next_num) if next_num >= 10 else next_num