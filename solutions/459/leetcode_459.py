#------------------------------------------------------
# Solution 1 - brute force
#------------------------------------------------------

# Runtime:  33.61%
# Memory:   75.62%


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)

        upper_limit = len_s // 2

        for substring_len in range(1, upper_limit + 1):
            substring = s[:substring_len]

            multiplier = len_s // substring_len
            
            test_s = substring * multiplier

            if s == test_s:
                return True

        return False


#------------------------------------------------------
# Solution 2 - tiling
#------------------------------------------------------

# Runtime:  98.12%
# Memory:   75.62%


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        test_s = s + s

        test_s = test_s[1:]
        test_s = test_s[:-1]

        return s in test_s
