#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  45.80%
# Memory:   78.65%


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        result = 1

        min_value = maxSum // n
        max_value = min_value + n

        left_count = index
        right_count = n - 1 - left_count

        @cache
        def sumElements(x, count):
            start_value = max(x - count + 1, 1)
            end_value = x

            return (start_value + end_value) * (count / 2)

        def isValid(x):
            val = x

            # Arithmetic sequence formula
            # sum = (A[1] + A[n]) * (n / 2)

            # end or flat <-- slope <-- index --> slope --> end or flat
            left_slope_index = max(index - (x - 1), 0)
            right_slope_index = min(index + x - 1, n - 1)

            left_slope_count = index - left_slope_index
            right_slope_count =  right_slope_index - index

            left_flat_count = left_slope_index
            right_flat_count = n - 1 - right_slope_index

            val += sumElements(x - 1, left_slope_count)
            val += sumElements(x - 1, right_slope_count)

            val += left_flat_count
            val += right_flat_count

            return val <= maxSum


        low = min_value
        high = max_value

        while low < high:
            mid = low + (high - low) // 2

            if isValid(mid):
                low = mid + 1
            else:
                high = mid

        return low - 1

        return min_value