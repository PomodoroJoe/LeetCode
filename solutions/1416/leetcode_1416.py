#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


from functools import cache

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        result = 0

        max_index = len(s) - 1

        n = []
        for c in s:
            n += [int(c)]


        @cache
        def numberOfArraysRecurse(index):
            if index > max_index:
                return 0

            if n[index] == 0:
                return 0

            result = 0

            prefix_index = index
            prefix_num = n[index]

            while prefix_num <= k and prefix_index <= max_index:
                prefix_index += 1
                result += numberOfArraysRecurse(prefix_index)

                if prefix_index > max_index:
                    break

                prefix_num = (prefix_num * 10) + n[prefix_index]

            if prefix_num and prefix_num <= k and prefix_index > max_index:
                result += 1
                
            return result


        result = numberOfArraysRecurse(0)
        return result % (pow(10, 9) + 7)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ internal mod
#------------------------------------------------------

# Runtime:  94.53%
# Memory:   23.69%


from functools import cache

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        result = 0

        max_index = len(s) - 1
        mod_num = (pow(10, 9) + 7)

        n = []
        for c in s:
            n += [int(c)]

        @cache
        def numberOfArraysRecurse(index):
            if index > max_index:
                return 0

            if n[index] == 0:
                return 0

            result = 0

            prefix_index = index
            prefix_num = n[index]

            while prefix_num <= k and prefix_index <= max_index:
                prefix_index += 1
                result += numberOfArraysRecurse(prefix_index)

                if prefix_index > max_index:
                    break

                prefix_num = (prefix_num * 10) + n[prefix_index]

            if prefix_num and prefix_num <= k and prefix_index > max_index:
                result += 1
                
            return result % mod_num


        result = numberOfArraysRecurse(0)
        return result % mod_num



#------------------------------------------------------
# Solution 3 - Solution 2 w/ zip
#------------------------------------------------------

# Runtime:  95.54%
# Memory:   23.61%


from functools import cache

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        result = 0

        max_index = len(s) - 1
        mod_num = (pow(10, 9) + 7)

        n = list(map(int, s))

        @cache
        def numberOfArraysRecurse(index):
            if index > max_index:
                return 0

            if n[index] == 0:
                return 0

            result = 0

            prefix_index = index
            prefix_num = n[index]

            while prefix_num <= k and prefix_index <= max_index:
                prefix_index += 1
                result += numberOfArraysRecurse(prefix_index)

                if prefix_index > max_index:
                    break

                prefix_num = (prefix_num * 10) + n[prefix_index]

            if prefix_num and prefix_num <= k and prefix_index > max_index:
                result += 1
                
            return result % mod_num


        result = numberOfArraysRecurse(0)
        return result % mod_num