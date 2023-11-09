#------------------------------------------------------
# Solution 1 - window/range
#------------------------------------------------------

# Runtime:  29.50%
# Memory:   77.34%


class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0

        s_len = len(s)

        start = 0
        end = 0

        while start < s_len:
            c = s[start]

            while end < s_len and s[end] == c:
                result += 1
                end += 1
            
            delta = end - start
            result += sum(range(1, delta))

            start = end

        return result % ((10 ** 9) + 7)



#------------------------------------------------------
# Solution 2 - current count
#------------------------------------------------------

# Runtime:  84.53%
# Memory:   30.58%


class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0

        prev_c = None
        current_count = 0

        for c in s:
            if c == prev_c:
                current_count += 1
            else:
                current_count = 1
                prev_c = c
                
            result += current_count

        return result % ((10 ** 9) + 7)