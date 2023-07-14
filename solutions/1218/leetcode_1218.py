#------------------------------------------------------
# Solution 1 - dp
#------------------------------------------------------

# Runtime:  29.59%
# Memory:   62.84%


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        result = 1

        # key = prev end val, value = longest subsequence ending at the end val
        dp = defaultdict(int)

        for n in arr:
            prev_n = n - difference
            prev_subsequence_len = dp[prev_n]

            dp[n] = prev_subsequence_len + 1
            result = max(result, dp[n])

        return result


#------------------------------------------------------
# Solution 2 - Solution 1 (optimized)
#------------------------------------------------------

# Runtime:  58.82%
# Memory:   92.78%


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        result = 1

        # key = prev end val, value = longest subsequence ending at the end val
        dp = defaultdict(int)

        for n in arr:
            dp[n] = dp[n - difference] + 1
            result = max(result, dp[n])

        return result


#------------------------------------------------------
# Solution 3 - Solution 2 w/ custom min
#------------------------------------------------------

# Runtime:  74.32%
# Memory:   62.84%


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        result = 1

        # key = prev end val, value = longest subsequence ending at the end val
        dp = defaultdict(int)

        for n in arr:
            dp[n] = dp[n - difference] + 1
            result = result if result > dp[n] else dp[n]

        return result