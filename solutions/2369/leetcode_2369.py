#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  78.46%
# Memory:    5.39%


class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        max_index = len(nums) - 1

        @cache
        def validPartitionRecurse(index):
            count = max_index - index + 1

            if count < 2:
                return False

            if count == 2:
                return nums[index] == nums[index + 1]

            if count == 3:
                option_1 = nums[index] == nums[index + 1] == nums[index + 2]
                option_2 = nums[index] == nums[index + 1] - 1 == nums[index + 2] - 2
                return option_1 or option_2

            option_1 = False
            option_2 = False
            option_3 = False

            # Option 1
            if nums[index] == nums[index + 1]:
                option_1 = validPartitionRecurse(index + 2)

            # Option 2
            if nums[index] == nums[index + 1] == nums[index + 2]:
                option_2 = validPartitionRecurse(index + 3)

            # Option 3
            if nums[index] == nums[index + 1] - 1 == nums[index + 2] - 2:
                option_3 = validPartitionRecurse(index + 3)

            return option_1 or option_2 or option_3


        return validPartitionRecurse(0)


#------------------------------------------------------
# Solution 2 - Solution 1 w/ early returns
#------------------------------------------------------

# Runtime:  93.80%
# Memory:   10.00%


class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        max_index = len(nums) - 1

        @cache
        def validPartitionRecurse(index):
            count = max_index - index + 1

            if count < 2:
                return False

            if count == 2:
                return nums[index] == nums[index + 1]

            if count == 3:
                option_1 = nums[index] == nums[index + 1] == nums[index + 2]
                option_2 = nums[index] == nums[index + 1] - 1 == nums[index + 2] - 2
                return option_1 or option_2

            # Option 1
            if nums[index] == nums[index + 1]:
                if validPartitionRecurse(index + 2):
                    return True

            # Option 2
            if nums[index] == nums[index + 1] == nums[index + 2]:
                if validPartitionRecurse(index + 3):
                    return True

            # Option 3
            if nums[index] == nums[index + 1] - 1 == nums[index + 2] - 2:
                if validPartitionRecurse(index + 3):
                    return True

            return False


        return validPartitionRecurse(0)