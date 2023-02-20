#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  71.20%
# Memory:   31.40%


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        mid = 0

        while left <= right:
            mid = left + ((right - left) // 2)

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left



#------------------------------------------------------
# Solution 2 - mid_val
#------------------------------------------------------

# Runtime:  88.60%
# Memory:   73.51%


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        mid = 0
        mid_val = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            mid_val = nums[mid]

            if target == mid_val:
                return mid

            if target > mid_val:
                left = mid + 1
            else:
                right = mid - 1

        return left



#------------------------------------------------------
# Solution 3 swap order of target compare
#------------------------------------------------------

# Runtime:  46.45%
# Memory:   31.40%


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        mid = 0
        mid_val = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            mid_val = nums[mid]

            if target == mid_val:
                return mid

            if mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return left



#------------------------------------------------------
# Solution 4 - minimize var names
#------------------------------------------------------

# Runtime:  71.20%
# Memory:   31.40%



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        m = 0
        v = 0

        while l <= r:
            m = l + ((r - l) // 2)
            v = nums[m]

            if target == v:
                return m

            if target > v:
                l = m + 1
            else:
                r = m - 1

        return l


#------------------------------------------------------
# Solution 5 - elif
#------------------------------------------------------

# Runtime:  99.62%
# Memory:   31.40%


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        mid = 0
        mid_val = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            mid_val = nums[mid]

            if target == mid_val:
                return mid
            elif target > mid_val:
                left = mid + 1
            else:
                right = mid - 1

        return left