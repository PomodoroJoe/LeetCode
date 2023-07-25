#------------------------------------------------------
# Solution 1 - recursive binary search
#------------------------------------------------------

# Runtime:  11.57%
# Memory:   10.29%


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def peakIndexInMountainArrayRecurse(left_index, right_index):
            if left_index == right_index:
                return left_index

            mid_index = left_index + ((right_index - left_index) // 2)

            mid_value = arr[mid_index]

            left_value = arr[mid_index - 1]
            right_value = arr[mid_index + 1]

            if left_value < mid_value and right_value < mid_value:
                return mid_index

            if left_value < mid_value:
                new_left_index = mid_index + 1
                return peakIndexInMountainArrayRecurse(new_left_index, right_index)

            new_right_index = mid_index
            return peakIndexInMountainArrayRecurse(left_index, new_right_index)

        
        return peakIndexInMountainArrayRecurse(0, len(arr) - 1)



#------------------------------------------------------
# Solution 2 - Solution 1 w/o helper vars
#------------------------------------------------------

# Runtime:  48.85%
# Memory:   10.29%


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def peakIndexInMountainArrayRecurse(left_index, right_index):
            if left_index == right_index:
                return left_index

            mid_index = left_index + ((right_index - left_index) // 2)

            mid_value = arr[mid_index]

            left_value = arr[mid_index - 1]
            right_value = arr[mid_index + 1]

            if left_value < mid_value and right_value < mid_value:
                return mid_index

            if left_value < mid_value:
                return peakIndexInMountainArrayRecurse(mid_index + 1, right_index)

            return peakIndexInMountainArrayRecurse(left_index, mid_index)

        return peakIndexInMountainArrayRecurse(0, len(arr) - 1)



#------------------------------------------------------
# Solution 3 - Solution 2 w/o more helper vars
#------------------------------------------------------

# Runtime:  46.65%
# Memory:   10.29%


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def peakIndexInMountainArrayRecurse(left_index, right_index):
            if left_index == right_index:
                return left_index

            mid_index = left_index + ((right_index - left_index) // 2)
            mid_value = arr[mid_index]

            if arr[mid_index - 1] < mid_value and arr[mid_index + 1] < mid_value:
                return mid_index

            if arr[mid_index - 1] < mid_value:
                return peakIndexInMountainArrayRecurse(mid_index + 1, right_index)

            return peakIndexInMountainArrayRecurse(left_index, mid_index)

        return peakIndexInMountainArrayRecurse(0, len(arr) - 1)



#------------------------------------------------------
# Solution 4 - Solution 3 w/o more helper vars
#------------------------------------------------------

# Runtime:  92.40%
# Memory:   10.29%


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def peakIndexInMountainArrayRecurse(left_index, right_index):
            if left_index == right_index:
                return left_index

            mid_index = left_index + ((right_index - left_index) // 2)

            if arr[mid_index - 1] < arr[mid_index] and arr[mid_index + 1] < arr[mid_index]:
                return mid_index

            if arr[mid_index - 1] < arr[mid_index]:
                return peakIndexInMountainArrayRecurse(mid_index + 1, right_index)

            return peakIndexInMountainArrayRecurse(left_index, mid_index)

        return peakIndexInMountainArrayRecurse(0, len(arr) - 1)