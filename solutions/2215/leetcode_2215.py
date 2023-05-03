#------------------------------------------------------
# Solution 1 - set difference
#------------------------------------------------------

# Runtime:  76.61%
# Memory:    9.53%


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]

        s1 = set(nums1)
        s2 = set(nums2)

        result[0] = s1 - s2
        result[1] = s2 - s1

        return result



#------------------------------------------------------
# Solution 2 - set difference (compact)
#------------------------------------------------------

# Runtime:  76.61%
# Memory:    9.53%


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        return [s1 - s2, s2 - s1]