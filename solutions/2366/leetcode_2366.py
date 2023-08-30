#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  62.81%
# Memory:   73.55%


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result = 0

        OP_COUNT = 0
        NEW_TARGET = 1

        # return (op_count, new_target)
        def splitNum(num, target):
            op_count = 0
            new_target = target

            if num % target == 0:
                op_count = (num // target) - 1
                new_target = target
            else:
                element_count = (num // target) + 1
                new_target = num // element_count
                op_count = element_count - 1

            return (op_count, new_target)


        nums_count = len(nums)
        target = nums[-1]

        for i in range(nums_count - 2, -1, -1):
            num = nums[i]

            if num <= target:
                target = num
                continue

            op_count, target = splitNum(num, target)
            result += op_count

        return result