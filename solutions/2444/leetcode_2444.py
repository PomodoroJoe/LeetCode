#------------------------------------------------------
# Solution 1 - brute force
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0

        for start in range(len(nums)):
            for end in range(start, len(nums)):

                min_num = inf
                max_num = -inf

                for i in range(start, end + 1):
                    min_num = min(min_num, nums[i])
                    max_num = max(max_num, nums[i])

                if min_num == minK and max_num == maxK:
                    result += 1

        return result




#------------------------------------------------------
# Solution 2 - building up subarrays
#------------------------------------------------------

# Runtime:  91.15%
# Memory:   69.18%


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0

        start_index = None
        
        min_index = None
        max_index = None

        for i, num in enumerate(nums):
            
            if num < minK or num > maxK:
                # start over
                start_index = None
                min_index = None
                max_index = None
                continue

            if start_index == None:
                start_index = i

            if num == minK:
                min_index = i

            if num == maxK:
                max_index = i

            # [n, n+1, n+2, ... , min_index, ... , max_index, ..., i]
            # (start_index) left_side <--> minK...maxk <--> right_side (i)

            if min_index != None and max_index != None:
                left_side_end = min(min_index, max_index)
                result += (left_side_end - start_index) + 1

        return result