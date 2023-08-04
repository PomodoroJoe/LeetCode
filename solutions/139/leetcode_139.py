#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def wordBreakRecurse(remaining_s):
            if remaining_s == "":
                return True

            if remaining_s in wordDict:
                return True

            if len(remaining_s) == 1:
                return False

            for split in range(1, len(remaining_s)):
                left = remaining_s[:split]
                right = remaining_s[split:]

                if left not in wordDict:
                    continue

                if wordBreakRecurse(right):
                    return True

            return False

        return wordBreakRecurse(s)


#------------------------------------------------------
# Solution 2 - Solution 1 w/ memoization
#------------------------------------------------------

# Runtime:  76.58%
# Memory:   10.57%


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = {}

        def wordBreakRecurse(remaining_s):
            key = remaining_s
            if key in dp:
                return dp[key]

            if remaining_s == "":
                dp[key] = True
                return True

            if remaining_s in wordDict:
                dp[key] = True
                return True

            if len(remaining_s) == 1:
                dp[key] = False
                return False

            for split in range(1, len(remaining_s)):
                left = remaining_s[:split]
                right = remaining_s[split:]

                if left not in wordDict:
                    continue

                if wordBreakRecurse(right):
                    dp[key] = True
                    return True

            dp[key] = False
            return False

        return wordBreakRecurse(s)


#------------------------------------------------------
# Solution 3 - Solution 2 w/ cache
#------------------------------------------------------

# Runtime:  64.41%
# Memory:   18.87%


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def wordBreakRecurse(remaining_s):
            if remaining_s == "":
                return True

            if remaining_s in wordDict:
                return True

            if len(remaining_s) == 1:
                return False

            for split in range(1, len(remaining_s)):
                left = remaining_s[:split]
                right = remaining_s[split:]

                if left not in wordDict:
                    continue

                if wordBreakRecurse(right):
                    return True

            return False

        return wordBreakRecurse(s)


#------------------------------------------------------
# Solution 4 - Solution 2 w/o continue
#------------------------------------------------------

# Runtime:  54.73%
# Memory:   18.87%


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = {}

        def wordBreakRecurse(remaining_s):
            key = remaining_s
            if key in dp:
                return dp[key]

            if remaining_s == "":
                dp[key] = True
                return True

            if remaining_s in wordDict:
                dp[key] = True
                return True

            if len(remaining_s) == 1:
                dp[key] = False
                return False

            for split in range(1, len(remaining_s)):
                left = remaining_s[:split]
                right = remaining_s[split:]

                if left in wordDict:
                    if wordBreakRecurse(right):
                        dp[key] = True
                        return True

            dp[key] = False
            return False

        return wordBreakRecurse(s)



#------------------------------------------------------
# Solution 6 - clean code
#------------------------------------------------------

# Runtime:  97.97%
# Memory:   18.87%


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def wordBreakRecurse(remaining_s):
            if remaining_s == "":
                return True

            if remaining_s in wordDict:
                return True

            if len(remaining_s) == 1:
                return False

            for split in range(1, len(remaining_s)):
                if remaining_s[:split] in wordDict:
                    if wordBreakRecurse(remaining_s[split:]):
                        return True

            return False

        return wordBreakRecurse(s)