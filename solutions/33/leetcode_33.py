#------------------------------------------------------
# Solution 1 - binary search
#------------------------------------------------------

# Runtime:  72.47%
# Memory:   72.11%


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower = 0
        upper = len(nums) - 1

        WRAP_UPPER = 1
        WRAP_LOWER = -1

        while lower <= upper:
            mid = lower + ((upper - lower) // 2)

            if nums[mid] == target:
                return mid

            if lower == upper:
                return -1

            wrap = None

            if nums[mid] > nums[upper]:
                wrap = WRAP_UPPER
            
            if nums[mid] < nums[lower]:
                wrap = WRAP_LOWER

            # Standard Binary Search
            if wrap == None:
                if target > nums[mid]:
                    lower = mid + 1
                else:
                    upper = mid
            
            # Wrap Upper
            if wrap == WRAP_UPPER:
                if target >= nums[lower] and target < nums[mid]:
                    upper = mid
                else:
                    lower = mid + 1

            # Wrap Lower
            if wrap == WRAP_LOWER:
                if target > nums[mid] and target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid
            
        return -1



#------------------------------------------------------
# Solution 6 - Solution 1 w/o wrap == None
#------------------------------------------------------

# Runtime:  97.13%
# Memory:   72.11%


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower = 0
        upper = len(nums) - 1

        WRAP_NONE = 0
        WRAP_UPPER = 1
        WRAP_LOWER = -1

        while lower <= upper:
            mid = lower + ((upper - lower) // 2)

            if nums[mid] == target:
                return mid

            if lower == upper:
                return -1

            wrap = WRAP_NONE
            if nums[mid] > nums[upper]:
                wrap = WRAP_UPPER

            if nums[mid] < nums[lower]:
                wrap = WRAP_LOWER


            if wrap == WRAP_NONE:
                if target > nums[mid]:
                    lower = mid + 1
                else:
                    upper = mid
            
            if wrap == WRAP_UPPER:
                if target >= nums[lower] and target < nums[mid]:
                    upper = mid
                else:
                    lower = mid + 1

            if wrap == WRAP_LOWER:
                if target > nums[mid] and target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid
            
        return -1