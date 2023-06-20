#------------------------------------------------------
# Solution 1 - sliding window with sum()
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        count = k + 1 + k

        if len(nums) < count:
            return [-1] * len(nums)

        low = 0
        high = count - 1

        result = [-1] * k

        while high < len(nums):
            val = sum(nums[low:high+1]) // count
            result.append(val)

            low += 1
            high += 1

        result += [-1] * k

        return result



#------------------------------------------------------
# Solution 2 - sliding window with updating total
#------------------------------------------------------

# Runtime:  97.50%
# Memory:   41.70%

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        count = k + 1 + k

        if len(nums) < count:
            return [-1] * len(nums)

        low = 0
        high = count - 1

        result = [-1] * k

        total = sum(nums[low:high])

        while high < len(nums):
            total += nums[high]
            
            val = total // count
            result.append(val)

            total -= nums[low]

            low += 1
            high += 1

        result += [-1] * k

        return result