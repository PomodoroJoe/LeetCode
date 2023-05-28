#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        max_index = len(cuts) - 1

        sorted_cuts = sorted(cuts)

        def minCostRecurse(stick_start, stick_end, cuts_start, cuts_end):
            result = inf

            if cuts_start > cuts_end:
                return 0

            cut_cost = stick_end - stick_start

            if cuts_start == cuts_end:
                return cut_cost

            for i in range(cuts_start, cuts_end + 1):
                cut = sorted_cuts[i]

                left_start = cuts_start
                left_end = i - 1

                right_start = i + 1
                right_end = cuts_end

                left_stick_cost =  minCostRecurse(stick_start, cut, left_start, left_end)
                right_stick_cost =  minCostRecurse(cut, stick_end, right_start, right_end)

                cost = left_stick_cost + right_stick_cost

                result = min(result, cost)

            return result + cut_cost

        return minCostRecurse(0, n, 0, len(cuts) - 1)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  56.85%
# Memory:    5.95%


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        max_index = len(cuts) - 1

        sorted_cuts = sorted(cuts)

        @cache
        def minCostRecurse(stick_start, stick_end, cuts_start, cuts_end):
            result = inf

            if cuts_start > cuts_end:
                return 0

            cut_cost = stick_end - stick_start

            if cuts_start == cuts_end:
                return cut_cost

            for i in range(cuts_start, cuts_end + 1):
                cut = sorted_cuts[i]

                left_start = cuts_start
                left_end = i - 1

                right_start = i + 1
                right_end = cuts_end

                left_stick_cost =  minCostRecurse(stick_start, cut, left_start, left_end)
                right_stick_cost =  minCostRecurse(cut, stick_end, right_start, right_end)

                cost = left_stick_cost + right_stick_cost

                result = min(result, cost)

            return result + cut_cost

        return minCostRecurse(0, n, 0, len(cuts) - 1)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ custom min
#------------------------------------------------------

# Runtime:  76.49%
# Memory:   14.88%