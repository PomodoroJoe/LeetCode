#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        result = 0

        sorted_events = sorted(events)
        max_index = len(events) - 1

        def maxValueRecurse(start_index, remaining_k):
            if start_index > max_index or remaining_k == 0:
                return 0

            # don't attend the event
            option_1 = maxValueRecurse(start_index + 1, remaining_k)

            # attend the event
            event = sorted_events[start_index]

            next_index = start_index + 1
            while next_index <= max_index and sorted_events[next_index][0] <= event[1]:
                next_index += 1

            option_2 = event[2] + maxValueRecurse(next_index, remaining_k - 1)

            return max(option_1, option_2)

        result = maxValueRecurse(0, k)
        return result


#------------------------------------------------------
# Solution 2 - Solution 1 w/ dp (memoization)
#------------------------------------------------------

# Runtime:  61.76%
# Memory:   35.29%


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        result = 0

        sorted_events = sorted(events)
        max_index = len(events) - 1

        dp = {}

        def maxValueRecurse(start_index, remaining_k):
            key = (start_index, remaining_k)
            if key in dp:
                return dp[key]

            if start_index > max_index or remaining_k == 0:
                dp[key] = 0
                return 0

            # don't attend the event
            option_1 = maxValueRecurse(start_index + 1, remaining_k)

            # attend the event
            event = sorted_events[start_index]

            next_index = start_index + 1
            while next_index <= max_index and sorted_events[next_index][0] <= event[1]:
                next_index += 1

            option_2 = event[2] + maxValueRecurse(next_index, remaining_k - 1)

            dp[key] = max(option_1, option_2)
            return dp[key]

        result = maxValueRecurse(0, k)
        return result


#------------------------------------------------------
# Solution 3 - Solution 1 w/ @cache
#------------------------------------------------------

# Runtime:  79.41%
# Memory:   31.62%


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        result = 0

        sorted_events = sorted(events)
        max_index = len(events) - 1

        @cache
        def maxValueRecurse(start_index, remaining_k):
            if start_index > max_index or remaining_k == 0:
                return 0

            # don't attend the event
            option_1 = maxValueRecurse(start_index + 1, remaining_k)

            # attend the event
            event = sorted_events[start_index]

            next_index = start_index + 1
            while next_index <= max_index and sorted_events[next_index][0] <= event[1]:
                next_index += 1

            option_2 = event[2] + maxValueRecurse(next_index, remaining_k - 1)

            return max(option_1, option_2)

        result = maxValueRecurse(0, k)
        return result


#------------------------------------------------------
# Solution 4 - Solution 3 w/ custom max
#------------------------------------------------------

# Runtime:  84.56%
# Memory:   28.68%


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        result = 0

        sorted_events = sorted(events)
        max_index = len(events) - 1

        @cache
        def maxValueRecurse(start_index, remaining_k):
            if start_index > max_index or remaining_k == 0:
                return 0

            # don't attend the event
            option_1 = maxValueRecurse(start_index + 1, remaining_k)

            # attend the event
            event = sorted_events[start_index]

            next_index = start_index + 1
            while next_index <= max_index and sorted_events[next_index][0] <= event[1]:
                next_index += 1

            option_2 = event[2] + maxValueRecurse(next_index, remaining_k - 1)

            return option_1 if option_1 > option_2 else option_2

        result = maxValueRecurse(0, k)
        return result



#------------------------------------------------------
# Solution 5 - Solution 4 w/ separate base cases
#------------------------------------------------------

# Runtime:  88.97%
# Memory:   30.15%


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        result = 0

        sorted_events = sorted(events)
        max_index = len(events) - 1

        @cache
        def maxValueRecurse(start_index, remaining_k):
            if start_index > max_index:
                return 0

            if remaining_k == 0:
                return 0

            option_1 = maxValueRecurse(start_index + 1, remaining_k)
            
            event = sorted_events[start_index]
            next_index = start_index + 1
            while next_index <= max_index and sorted_events[next_index][0] <= event[1]:
                next_index += 1
            option_2 = event[2] + maxValueRecurse(next_index, remaining_k - 1)

            return option_1 if option_1 > option_2 else option_2

        result = maxValueRecurse(0, k)
        return result