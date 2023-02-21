#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  97.57%
# Memory:   39.30%


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0

        low = 0
        high = len(nums) - 1

        mid = 0

        while low < high:
            mid = low + ((high - low) // 2)
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]