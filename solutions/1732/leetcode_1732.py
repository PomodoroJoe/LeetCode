#------------------------------------------------------
# Solution 1 - running sum
#------------------------------------------------------

# Runtime:  16.50%
# Memory:   26.60%


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        running_sum = 0

        for delta in gain:
            running_sum += delta
            result = max(result, running_sum)

        return result


#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  46.24%
# Memory:   66.27%


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        running_sum = 0

        for delta in gain:
            running_sum += delta
            result = result if result > running_sum else running_sum

        return result


#------------------------------------------------------
# Solution 3
#------------------------------------------------------

# Runtime:  78.50%
# Memory:   26.60%


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        total = 0

        for n in gain:
            total += n
            result = result if result > total else total

        return result


#------------------------------------------------------
# Solution 4
#------------------------------------------------------

# Runtime:  83.93%
# Memory:   66.27%


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        r, t = 0, 0
        for n in gain:
            t += n
            r = r if r > t else t
        return r



#------------------------------------------------------
# Solution 5
#------------------------------------------------------

# Runtime:  29.15%
# Memory:   91.15%


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        r, t = 0, 0
        for n in gain:
            t += n
            r = max(r, t)
        return r