#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  93.95%
# Memory:   47.70%


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        result = 0

        # index = span_start, value = span_end
        spans = [0] * (n + 1)
        for pos, reach in enumerate(ranges):
            span_start = pos - reach if pos > reach else 0
            span_end = pos + reach if pos + reach < n else n
            spans[span_start] = max(span_end, spans[span_start])

        current_span_end = 0
        next_span_option_end = 0

        for pos in range(n + 1):
            span_start = pos
            span_end = spans[span_start]

            if span_start > next_span_option_end:
                return -1

            if span_start > current_span_end:
                current_span_end = next_span_option_end
                result += 1

            if span_end > next_span_option_end:
                next_span_option_end = span_end

        return result