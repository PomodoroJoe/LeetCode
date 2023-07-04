#------------------------------------------------------
# Solution 1 - medium solution (not linear runtime)
#------------------------------------------------------

# Runtime:  19.29%
# Memory:   86.82%


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = sum(nums)

        def is_the_answer(option):
            count = 0
            for n in nums:
                if n == option:
                    count += 1
            return count == 1

        for n in nums:
            sub_total = total - n
            if sub_total % 3 == 0:
                if is_the_answer(n):
                    return n


#------------------------------------------------------
# Solution 2 - hard solution (linear runtime)
#------------------------------------------------------

# Runtime:  84.27%
# Memory:   86.82%


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        flip_count_ones = 0
        flip_count_twos = 0

        for n in nums:
            flip_count_ones = (flip_count_ones ^ n) & (~flip_count_twos)
            flip_count_twos = (flip_count_twos ^ n) & (~flip_count_ones)

        return flip_count_ones