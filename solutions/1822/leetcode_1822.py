#------------------------------------------------------
# Solution 1 - flip result
#------------------------------------------------------

# Runtime:  93.42%
# Memory:    7.53%


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1

        for num in nums:
            if num < 0:
                result = -1 * result

            if num == 0:
                return 0

        return result



#------------------------------------------------------
# Solution 2 - count % 2
#------------------------------------------------------

# Runtime:  66.50%
# Memory:    7.53%


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if num < 0:
                count += 1

            if num == 0:
                return 0

        return -1 if count % 2 == 1 else 1