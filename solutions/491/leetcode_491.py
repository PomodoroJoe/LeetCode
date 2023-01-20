#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  82.60%
# Memory:   19.50%


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def findSubsequencesRecurse(nums):
            result = []

            # base case
            if len(nums) < 2:
                return [nums]

            num = nums[0]
            result.append([num])

            subsequences = findSubsequencesRecurse(nums[1:])

            for subsequence in subsequences:
                if len(subsequence) < 1:
                    continue

                if num <= subsequence[0]:
                    result.append([num] + subsequence)

                result.append(subsequence)

            return result


        all_subsequence = findSubsequencesRecurse(nums)

        valid_subsequences = set()
        for subsequence in all_subsequence:
            if len(subsequence) < 2:
                continue
            valid_subsequences.add(tuple(subsequence))

        return list(valid_subsequences)



#------------------------------------------------------
# Solution 2 - iterative w/ set union
#------------------------------------------------------

# Runtime:  93.20%
# Memory:   95.71%

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        index = len(nums) - 1

        result = set()

        while index >= 0:
            num = nums[index]
            working_set = set()
            working_set.add(tuple([num]))

            for sub in result:
                if num <= sub[0]:
                    working_set.add(tuple([num] + list(sub)))

            result = result.union(working_set)
            index -= 1


        final_result = []
        for sub in result:
            if len(sub) < 2:
                continue
            final_result.append(sub)

        return final_result
