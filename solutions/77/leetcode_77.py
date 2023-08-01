#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  77.20%
# Memory:    6.98%


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combineRecurse(start, remaining_k):
            if remaining_k == 0:
                return [[]]

            result = []

            for i in range(start, n + 1):
                prefix = [i]

                suffixes = combineRecurse(i + 1, remaining_k - 1)
                for suffix in suffixes:
                    option = [] + prefix + suffix
                    result.append(option)

            return result

        return combineRecurse(1, k)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ Cache
#------------------------------------------------------

# Runtime:  97.55%
# Memory:    6.98%


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        @cache
        def combineRecurse(start, remaining_k):
            if remaining_k == 0:
                return [[]]

            result = []

            for i in range(start, n + 1):
                prefix = [i]

                suffixes = combineRecurse(i + 1, remaining_k - 1)
                for suffix in suffixes:
                    option = [] + prefix + suffix
                    result.append(option)

            return result

        return combineRecurse(1, k)


#------------------------------------------------------
# Solution 3 - Solution 2 w/ better option
#------------------------------------------------------

# Runtime:  99.80%
# Memory:    6.98%


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        @cache
        def combineRecurse(start, remaining_k):
            if remaining_k == 0:
                return [[]]

            result = []

            for i in range(start, n + 1):
                prefix = [i]

                suffixes = combineRecurse(i + 1, remaining_k - 1)
                for suffix in suffixes:
                    option = prefix + suffix
                    result.append(option)

            return result

        return combineRecurse(1, k)


#------------------------------------------------------
# Solution 4 - shortcut (itertools combinations)
#------------------------------------------------------

# Runtime: 100.00%
# Memory:   98.92%


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1, n + 1), k)