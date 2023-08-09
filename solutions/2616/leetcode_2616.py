#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        sorted_nums = sorted(nums)

        deltas = []
        for i in range(1, len(sorted_nums)):
            delta = sorted_nums[i] - sorted_nums[i - 1]
            deltas.append(delta)

        def minimizeMaxRecurse(index, remaining_p, max_delta):
            if remaining_p == 0:
                return max_delta

            if index >= len(deltas):
                return inf

            # Option 1: don't use this delta
            option_1 = minimizeMaxRecurse(index + 1, remaining_p, max_delta)

            # Option 2: use this delta
            delta = deltas[index]
            new_max_delta = max(delta, max_delta)

            option_2 = minimizeMaxRecurse(index + 2, remaining_p - 1, new_max_delta)

            return min(option_1, option_2)

        return minimizeMaxRecurse(0, p, 0)


#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# MEMORY LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        sorted_nums = sorted(nums)

        deltas = []
        for i in range(1, len(sorted_nums)):
            delta = sorted_nums[i] - sorted_nums[i - 1]
            deltas.append(delta)

        @cache
        def minimizeMaxRecurse(index, remaining_p, max_delta):
            if remaining_p == 0:
                return max_delta

            if index >= len(deltas):
                return inf

            # Option 1: don't use this delta
            option_1 = minimizeMaxRecurse(index + 1, remaining_p, max_delta)

            # Option 2: use this delta
            delta = deltas[index]
            new_max_delta = max(delta, max_delta)

            option_2 = minimizeMaxRecurse(index + 2, remaining_p - 1, new_max_delta)

            return min(option_1, option_2)

        return minimizeMaxRecurse(0, p, 0)



#------------------------------------------------------
# Solution 3 - binary search
#------------------------------------------------------

# Runtime:  99.35%
# Memory:   78.60%


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if not nums or p == 0:
            return 0

        sorted_nums = sorted(nums)

        deltas = []
        for i in range(1, len(sorted_nums)):
            delta = sorted_nums[i] - sorted_nums[i - 1]
            deltas.append(delta)


        def countPairs(target_delta):
            result = 0
            index = 0

            while index < len(deltas):
                if deltas[index] <= target_delta:
                    result += 1
                    index += 1
                index += 1

            return result


        lower = 0
        upper = max(deltas)

        while lower < upper:
            mid = lower + (upper - lower) // 2

            pairs = countPairs(mid)

            if pairs >= p:
                upper = mid
            else:
                lower = mid + 1

        return lower
