#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  25.74%
# Memory:   13.22%


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def combinationSum4Recurse(target):
            if target == 0:
                return 1

            if target < 0:
                return 0

            result = 0
            for n in nums:
                new_target = target - n
                result += combinationSum4Recurse(new_target)
            return result

        return combinationSum4Recurse(target)



#------------------------------------------------------
# Solution 2 - Solution 1 w/o helper var
#------------------------------------------------------

# Runtime:  32.17%
# Memory:    6.40%


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def combinationSum4Recurse(target):
            if target == 0:
                return 1

            if target < 0:
                return 0

            result = 0
            for n in nums:
                result += combinationSum4Recurse(target - n)
            return result

        return combinationSum4Recurse(target)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ swapped base case order
#------------------------------------------------------

# Runtime:  60.38%
# Memory:    9.75%


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def combinationSum4Recurse(target):
            if target < 0:
                return 0

            if target == 0:
                return 1

            result = 0
            for n in nums:
                result += combinationSum4Recurse(target - n)
            return result

        return combinationSum4Recurse(target)