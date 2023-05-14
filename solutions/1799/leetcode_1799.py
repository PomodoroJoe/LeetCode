#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  82.60%
# Memory:   19.50%


from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        def maxScoreRecurse(remaining_nums, remaining_ops):
            if not remaining_nums or not remaining_ops:
                return 0

            result = 0
            len_nums = len(remaining_nums)

            for i in range(len_nums):
                for j in range(i+1, len_nums):
                    val = remaining_ops * gcd(remaining_nums[i], remaining_nums[j])

                    new_nums = remaining_nums.copy()
                    new_nums.pop(j)
                    new_nums.pop(i)

                    val += maxScoreRecurse(new_nums, remaining_ops - 1)

                    result = max(result, val)

            return result


        return maxScoreRecurse(nums, len(nums) // 2)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ tuples & cache
#------------------------------------------------------

# Runtime:  87.97%
# Memory:    8.86%


from functools import cache
from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def maxScoreRecurse(remaining_nums, remaining_ops):
            if not remaining_nums or not remaining_ops:
                return 0

            result = 0
            len_nums = len(remaining_nums)

            for i in range(len_nums):
                for j in range(i+1, len_nums):
                    val = remaining_ops * gcd(remaining_nums[i], remaining_nums[j])
                    new_nums = remaining_nums[:i] + remaining_nums[i+1:j] + remaining_nums[j+1:]
                    val += maxScoreRecurse(new_nums, remaining_ops - 1)

                    result = max(result, val)

            return result

        return maxScoreRecurse(tuple(nums), len(nums) // 2)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ custom gcd
#------------------------------------------------------

# Runtime:  94.30%
# Memory:    8.86%

from functools import cache

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x

        @cache
        def maxScoreRecurse(cur_nums, ops):
            if not cur_nums or not ops:
                return 0

            result = 0
            len_nums = len(cur_nums)

            for i in range(len_nums):
                for j in range(i+1, len_nums):
                    val = ops * gcd(cur_nums[i], cur_nums[j])
                    new_nums = cur_nums[:i] + cur_nums[i+1:j] + cur_nums[j+1:]
                    val += maxScoreRecurse(new_nums, ops - 1)

                    result = result if result > val else val

            return result

        return maxScoreRecurse(tuple(nums), len(nums) // 2)