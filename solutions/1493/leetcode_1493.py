#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  97.54%
# Memory:   72.32%


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0

        prev_group_count = 0
        group_count = 0

        removed_element = False

        for n in nums:
            if n == 1:
                group_count += 1
            else:
                removed_element = True

                option = group_count + prev_group_count
                result = option if option > result else result

                prev_group_count = group_count
                group_count = 0

        option = group_count + prev_group_count
        result = option if option > result else result

        if removed_element == False:
            result -= 1

        return result