#------------------------------------------------------
# Solution 1 - sorted intervals
#------------------------------------------------------

# Runtime:  46.42%
# Memory:   78.77%


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        sorted_intervals = sorted(intervals)
        prev_end = sorted_intervals[0][1]

        for interval in sorted_intervals[1:]:
            if interval[0] >= prev_end:
                prev_end = interval[1]
                continue

            result += 1
            prev_end = min(prev_end, interval[1])

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ custom min
#------------------------------------------------------

# Runtime:  51.36%
# Memory:   78.77%


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        sorted_intervals = sorted(intervals)
        prev_end = sorted_intervals[0][1]

        for interval in sorted_intervals[1:]:
            if interval[0] >= prev_end:
                prev_end = interval[1]
                continue

            result += 1
            prev_end = prev_end if prev_end < interval[1] else interval[1]

        return result