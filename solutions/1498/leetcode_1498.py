#------------------------------------------------------
# Solution 1 - min/max index
#------------------------------------------------------

# Runtime:  52.14%
# Memory:    6.91%


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        result = 0

        sorted_nums = sorted(nums)
        low = 0
        high = len(nums) - 1

        while low <= high:
            min_val = sorted_nums[low]
            max_val = sorted_nums[high]

            if min_val + max_val <= target:
                result += pow(2, high - low)
                low += 1
            else:
                high -= 1

        return result % (pow(10, 9) + 7)