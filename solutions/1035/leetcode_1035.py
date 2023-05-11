#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        if not nums1 or not nums2:
            return 0

        option_1 = self.maxUncrossedLines(nums1[1:], nums2)
        option_2 = 0

        n = nums1[0]
        if n in nums2:
            index = nums2.index(n)
            option_2 = 1 + self.maxUncrossedLines(nums1[1:], nums2[index + 1:])

        result = max(option_1, option_2)
        return result



#------------------------------------------------------
# Solution 2 - recursive w/ caching
#------------------------------------------------------

# Runtime:  32.81%
# Memory:   17.60%


from functools import cache

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        max_index_1 = len(nums1) - 1
        max_index_2 = len(nums2) - 1

        @cache
        def maxUncrossedLinesRecurse(i1, i2):

            if i1 > max_index_1 or i2 > max_index_2:
                return 0

            option_1 = maxUncrossedLinesRecurse(i1 + 1, i2)
            option_2 = 0

            n = nums1[i1]
            if n in nums2[i2:]:
                index = i2 + nums2[i2:].index(n)
                option_2 = 1 + maxUncrossedLinesRecurse(i1 + 1, index + 1)

            return max(option_1, option_2)

        return maxUncrossedLinesRecurse(0, 0)



#------------------------------------------------------
# Solution 3 - Solution 2 with index mapping
#------------------------------------------------------

# Runtime:  88.98%
# Memory:   17.60%


from functools import cache

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        max_index_1 = len(nums1) - 1
        max_index_2 = len(nums2) - 1

        mapping = defaultdict(list)
        for i, n in enumerate(nums2):
            mapping[n].append(i)

        def findIndex(n, start):
            if n not in mapping:
                return None

            for index in mapping[n]:
                if index >= start:
                    return index
            return None


        @cache
        def maxUncrossedLinesRecurse(i1, i2):

            if i1 > max_index_1 or i2 > max_index_2:
                return 0

            option_1 = maxUncrossedLinesRecurse(i1 + 1, i2)
            option_2 = 0

            n = nums1[i1]
            index = findIndex(n, i2)

            if index != None:
                option_2 = 1 + maxUncrossedLinesRecurse(i1 + 1, index + 1)

            return max(option_1, option_2)

        return maxUncrossedLinesRecurse(0, 0)