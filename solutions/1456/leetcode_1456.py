#------------------------------------------------------
# Solution 1 - sliding window
#------------------------------------------------------

# Runtime:  68.69%
# Memory:   14.59%


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        len_s = len(s)
        vowels = "aeiou"

        low = 0
        high = 0

        count = 0

        # init window
        while high < len_s and high < k:
            if s[high] in vowels:
                count += 1
            high += 1

        result = count

        # slide window
        while high < len_s:
            if s[high] in vowels:
                count += 1

            if s[low] in vowels:
                count -= 1

            result = max(result, count)

            low += 1
            high += 1

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ custom max
#------------------------------------------------------

# Runtime:  95.10%
# Memory:   14.59%


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        len_s = len(s)
        vowels = "aeiou"

        low = 0
        high = 0

        count = 0

        # init window
        while high < len_s and high < k:
            if s[high] in vowels:
                count += 1
            high += 1

        result = count

        # slide window
        while high < len_s:
            if s[high] in vowels:
                count += 1

            if s[low] in vowels:
                count -= 1

            result = count if count > result else result

            low += 1
            high += 1

        return result