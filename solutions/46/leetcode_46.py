#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  78.42%
# Memory:   72.39%


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permuteRecurse(remaining_nums):
            if not remaining_nums:
                return [[]]

            result = []

            for num in remaining_nums:
                permutation = [num]

                new_remaining_nums = remaining_nums.copy()
                new_remaining_nums.remove(num)

                suffixes = permuteRecurse(new_remaining_nums)
                for suffix in suffixes:
                    option = permutation + suffix
                    result.append(option)

            return result


        return permuteRecurse(nums)


#------------------------------------------------------
# Solution 2 - Solution 1 w/o helper vars
#------------------------------------------------------

# Runtime:  93.50%
# Memory:   91.92%


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permuteRecurse(remaining_nums):
            if not remaining_nums:
                return [[]]

            result = []

            for num in remaining_nums:
                new_remaining_nums = remaining_nums.copy()
                new_remaining_nums.remove(num)

                suffixes = permuteRecurse(new_remaining_nums)
                for suffix in suffixes:
                    option = [num] + suffix
                    result.append(option)

            return result


        return permuteRecurse(nums)



#------------------------------------------------------
# Solution 3 - itertools permutations
#------------------------------------------------------

# Runtime:  88.88%
# Memory:   91.92%


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       return permutations(nums)