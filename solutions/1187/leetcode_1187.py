#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        sorted_arr2 = sorted(arr2)

        def makeArrayIncreasingRecurse(i1, i2, next_val, count):
            if i1 < 0:
                return count

            val = arr1[i1]

            # option 1: keep element
            op1 = inf
            if val < next_val:
                op1 = makeArrayIncreasingRecurse(i1 - 1, i2, val, count)

            # option 2: replace element with largest remaining element in arr2
            op2 = inf

            swap_index = i2
            while swap_index > 0 and sorted_arr2[swap_index] >= next_val:
                swap_index -= 1

            if sorted_arr2[swap_index] < next_val:
                new_val = sorted_arr2[swap_index]
                op2 = makeArrayIncreasingRecurse(i1 - 1, swap_index - 1, new_val, count + 1)

            return op1 if op1 < op2 else op2

        result = makeArrayIncreasingRecurse(len(arr1) - 1, len(sorted_arr2) - 1, inf, 0)
        return result if result != inf else -1



#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache and removed count
#------------------------------------------------------

# Runtime:   5.39%
# Memory:    6.15%


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        sorted_arr2 = sorted(arr2)

        @cache
        def makeArrayIncreasingRecurse(i1, i2, next_val):
            if i1 < 0:
                return 0

            val = arr1[i1]

            # option 1: keep element
            op1 = inf
            if val < next_val:
                op1 = makeArrayIncreasingRecurse(i1 - 1, i2, val)

            # option 2: replace element with largest remaining element in arr2
            op2 = inf

            swap_index = i2
            while swap_index > 0 and sorted_arr2[swap_index] >= next_val:
                swap_index -= 1

            if sorted_arr2[swap_index] < next_val:
                new_val = sorted_arr2[swap_index]
                op2 = 1 + makeArrayIncreasingRecurse(i1 - 1, swap_index - 1, new_val)

            return op1 if op1 < op2 else op2

        result = makeArrayIncreasingRecurse(len(arr1) - 1, len(sorted_arr2) - 1, inf)
        return result if result != inf else -1



#------------------------------------------------------
# Solution 3 - Solution 2 w/ index binary search
#------------------------------------------------------

# Runtime:   7.70%
# Memory:    6.15%


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        sorted_arr2 = sorted(arr2)

        def findValueIndex(i2, next_val):
            low = 0
            high = i2

            while low < high:
                mid = low + (high - low) // 2
                
                if sorted_arr2[mid] < next_val:
                    low = mid + 1
                else:
                    high = mid

            return low if sorted_arr2[low] < next_val else low - 1


        @cache
        def makeArrayIncreasingRecurse(i1, i2, next_val):
            if i1 < 0:
                return 0

            val = arr1[i1]

            # option 1: keep element
            op1 = inf
            if val < next_val:
                op1 = makeArrayIncreasingRecurse(i1 - 1, i2, val)

            # option 2: replace element with largest remaining element in arr2
            op2 = inf

            swap_index = findValueIndex(i2, next_val)

            if sorted_arr2[swap_index] < next_val:
                new_val = sorted_arr2[swap_index]
                op2 = 1 + makeArrayIncreasingRecurse(i1 - 1, swap_index - 1, new_val)

            return op1 if op1 < op2 else op2

        result = makeArrayIncreasingRecurse(len(arr1) - 1, len(sorted_arr2) - 1, inf)
        return result if result != inf else -1




#------------------------------------------------------
# Solution 4 - Solution 3 w/ better caching (fewer args)
#------------------------------------------------------

# Runtime:  10.77%
# Memory:   15.39%


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        sorted_arr2 = sorted(arr2)

        def findValueIndex(next_val):
            low = 0
            high = len(sorted_arr2) - 1

            while low < high:
                mid = low + (high - low) // 2
                
                if sorted_arr2[mid] < next_val:
                    low = mid + 1
                else:
                    high = mid

            return low if sorted_arr2[low] < next_val else low - 1


        @cache
        def makeArrayIncreasingRecurse(i1, next_val):
            if i1 < 0:
                return 0

            val = arr1[i1]

            # option 1: keep element
            op1 = inf
            if val < next_val:
                op1 = makeArrayIncreasingRecurse(i1 - 1, val)

            # option 2: replace element with largest remaining element in arr2
            op2 = inf

            swap_index = findValueIndex(next_val)

            if sorted_arr2[swap_index] < next_val:
                new_val = sorted_arr2[swap_index]
                op2 = 1 + makeArrayIncreasingRecurse(i1 - 1, new_val)

            return op1 if op1 < op2 else op2

        result = makeArrayIncreasingRecurse(len(arr1) - 1, inf)
        return result if result != inf else -1


#------------------------------------------------------
# Solution 5 - Solution 4 w/ arr2 set
#------------------------------------------------------

# Runtime:  62.31%
# Memory:   15.39%


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        arr2_set = set(arr2)
        sorted_arr2 = sorted(arr2_set)

        @cache
        def findValueIndex(next_val):
            low = 0
            high = len(sorted_arr2) - 1

            while low < high:
                mid = low + (high - low) // 2
                
                if sorted_arr2[mid] < next_val:
                    low = mid + 1
                else:
                    high = mid

            return low if sorted_arr2[low] < next_val else low - 1


        @cache
        def makeArrayIncreasingRecurse(i1, next_val):
            if i1 < 0:
                return 0

            val = arr1[i1]

            # option 1: keep element
            op1 = inf
            if val < next_val:
                op1 = makeArrayIncreasingRecurse(i1 - 1, val)

            # option 2: replace element with largest remaining element in arr2
            op2 = inf

            swap_index = findValueIndex(next_val)

            if sorted_arr2[swap_index] < next_val:
                new_val = sorted_arr2[swap_index]
                op2 = 1 + makeArrayIncreasingRecurse(i1 - 1, new_val)

            return op1 if op1 < op2 else op2

        result = makeArrayIncreasingRecurse(len(arr1) - 1, inf)
        return result if result != inf else -1