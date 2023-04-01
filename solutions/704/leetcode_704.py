#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  51.88%
# Memory:   58.66%


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = len(nums)

        if count == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        mid_index = count // 2

        if target < nums[mid_index]:
            left = nums[:mid_index]
            return self.search(left, target)
        else:
            right = nums[mid_index:]
            result = self.search(right, target)

            if result == -1:
                return result
            else:
                return mid_index + result



#------------------------------------------------------
# Solution 2 - iterative
#------------------------------------------------------

# Runtime:  64.15%
# Memory:   58.66%


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + ((high - low) // 2)

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return -1 if nums[low] != target else low



#------------------------------------------------------
# Solution 3 - iterative w/ better index update
#------------------------------------------------------

# Runtime:  72.20%
# Memory:   13.84%


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return -1 if nums[low] != target else low