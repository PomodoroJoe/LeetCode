#------------------------------------------------------
# Solution 1 - brute force
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = inf

        for start in range(len(nums)):
            total = 0
            for end in range(start, len(nums)):
                total += nums[end]

                if total >= target:
                    sub_array_len = (end - start) + 1
                    result = min(result, sub_array_len)

        return result if result != inf else 0



#------------------------------------------------------
# Solution 2 - variable size sliding window
#------------------------------------------------------

# Runtime:  71.30%
# Memory:   81.67%


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = inf

        start = 0
        total = 0

        for end in range(len(nums)):
            total += nums[end]

            while total >= target:
                result = min(result, (end - start) + 1)

                total -= nums[start]
                start += 1
           
        return result if result != inf else 0



#------------------------------------------------------
# Solution 3 - Solution 2 w/ custom min
#------------------------------------------------------

# Runtime:  97.00%
# Memory:   81.67%


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = inf

        start = 0
        total = 0

        for end in range(len(nums)):
            total += nums[end]

            while total >= target:
                option = (end - start) + 1
                result = option if option < result else result

                total -= nums[start]
                start += 1
           
        return result if result != inf else 0