#------------------------------------------------------
# Solution 1 - missing nums array
#------------------------------------------------------

# Runtime:  85.86%
# Memory:   98.30%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected_number = 1

        missing_numbers = []

        index = 0

        while len(missing_numbers) < k:
            if index >= len(arr) or arr[index] != expected_number:
                missing_numbers.append(expected_number)
            else:
                index += 1

            expected_number += 1

        return missing_numbers[-1]



#------------------------------------------------------
# Solution 2 - missing number count
#------------------------------------------------------

# Runtime:  83.18%
# Memory:   80.25%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected_number = 1

        missing_numbers_count = 0

        index = 0

        while missing_numbers_count < k:
            if index >= len(arr) or arr[index] != expected_number:
                missing_numbers_count += 1
            else:
                index += 1

            expected_number += 1

        return expected_number - 1



#------------------------------------------------------
# Solution 3 - index
#------------------------------------------------------

# Runtime:  42.79%
# Memory:   98.30%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = 0

        expected_value = index + 1

        while index < len(arr) and arr[index] - expected_value < k:
            index += 1
            expected_value = index + 1

        return index + k


#------------------------------------------------------
# Solution 4 - binary search
#------------------------------------------------------

# Runtime:  95.52%
# Memory:   98.30%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1

        while high >= low:
            mid = low + ((high - low) // 2)
            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k



#------------------------------------------------------
# Solution 5 - index with helper values
#------------------------------------------------------

# Runtime:  47.27%
# Memory:   80.25%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = 0
        expected_value = index + 1

        delta = arr[index] - expected_value

        while delta < k and index < len(arr):
            index += 1
            expected_value = index + 1

            if index < len(arr):
                delta = arr[index] - expected_value

        return index + k



#------------------------------------------------------
# Solution 6 - index simplified
#------------------------------------------------------

# Runtime:  60.32%
# Memory:   80.25%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = 0

        while index < len(arr) and arr[index] - (index + 1) < k:
            index += 1

        return index + k



#------------------------------------------------------
# Solution 7 - binary search 2
#------------------------------------------------------

# Runtime:  88.69%
# Memory:   80.25%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1

        while high >= low:
            mid = low + ((high - low) // 2)

            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k


#------------------------------------------------------
# Solution 8 - binary search 3
#------------------------------------------------------

# Runtime:  83.18%
# Memory:   80.25%


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1

        while high >= low:
            mid = low + ((high - low) // 2)
            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k
