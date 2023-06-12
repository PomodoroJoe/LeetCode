#------------------------------------------------------
#
# LeetCode is down for maintenance at the moment so...
#
# Solution 1 and Solution 3 are not available.  Sorry.
#
#------------------------------------------------------

#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  66.23%
# Memory:   64.73%


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if not nums:
            return result

        
        def getRangeString(start, end):
            if start == end:
                return str(start)
            return str(start) + "->" + str(end)

        
        start = None
        end = None

        for num in nums:
            if start == None:
                start = num
                end = num
                continue

            if num > end + 1:
                val = getRangeString(start, end)
                result.append(val)

                start = num

            end = num

        val = getRangeString(start, end)
        result.append(val)

        return result