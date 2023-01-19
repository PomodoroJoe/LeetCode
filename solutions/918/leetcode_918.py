#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  56.65%
# Memory:   43.20%


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        result = nums[0]
        min_result = nums[0]

        current_max = nums[0]
        current_min = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            option_A = current_max + nums[i]
            option_B = nums[i]

            option_C = current_min + nums[i]

            current_max = max(option_A, option_B)
            current_min = min(option_C, option_B)

            result = max(result, current_max)
            min_result = min(min_result, current_min)

            total += nums[i]

        subtract_min_option = total - min_result

        if subtract_min_option != 0:
            result = max(result, subtract_min_option)

        return result
