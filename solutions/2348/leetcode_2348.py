#------------------------------------------------------
# Solution 1 - ranges
#------------------------------------------------------

# Runtime:  13.70%
# Memory:   07.77%


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0

        subarray_ranges = []
        current_range = []  # [start_index, end_index]

        for i, n in enumerate(nums):
            if n == 0:
                if current_range == []:
                    current_range = [i, i]
                else:
                    current_range[1] = i
            else:
                if current_range != []:
                    subarray_ranges.append(current_range)
                    current_range = []

        if current_range != []:
            subarray_ranges.append(current_range)

        for subarray_range in subarray_ranges:
            range_len = subarray_range[1] - subarray_range[0] + 1
            result += sum(range(range_len + 1))

        return result



#------------------------------------------------------
# Solution 2 - ranges w/ while loop sum
#------------------------------------------------------

# Runtime:  18.73%
# Memory:   07.77%


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0

        subarray_ranges = []
        current_range = []  # [start_index, end_index]

        for i, n in enumerate(nums):
            if n == 0:
                if current_range == []:
                    current_range = [i, i]
                else:
                    current_range[1] = i
            else:
                if current_range != []:
                    subarray_ranges.append(current_range)
                    current_range = []

        if current_range != []:
            subarray_ranges.append(current_range)

        for subarray_range in subarray_ranges:
            range_len = subarray_range[1] - subarray_range[0] + 1
            while range_len > 0:
                result += range_len
                range_len -= 1

        return result


#------------------------------------------------------
# Solution 3 - ranges w/ immediate result calculation
#------------------------------------------------------

# Runtime:  14.49%
# Memory:   07.77%


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0

        current_range = []  # [start_index, end_index]

        for i, n in enumerate(nums):
            if n == 0:
                if current_range == []:
                    current_range = [i, i]
                else:
                    current_range[1] = i
            else:
                if current_range != []:
                    range_len = current_range[1] - current_range[0] + 1
                    while range_len > 0:
                        result += range_len
                        range_len -= 1
                    
                    current_range = []

        if current_range != []:
            range_len = current_range[1] - current_range[0] + 1
            while range_len > 0:
                result += range_len
                range_len -= 1

        return result


#------------------------------------------------------
# Solution 4 - zero count
#------------------------------------------------------

# Runtime:  88.69%
# Memory:   78.90%


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0

        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
                result += zero_count
            else:
                zero_count = 0

        return result


#------------------------------------------------------
# Solution 5 - zero count w/ short names
#------------------------------------------------------

# Runtime:  96.47%
# Memory:   30.39%


lass Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for n in nums:
            if n == 0:
                count += 1
                result += count
            else:
                count = 0

        return result