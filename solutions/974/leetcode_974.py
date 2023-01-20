#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  62.51%
# Memory:   96.27%

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0

        prefix_remainder = []
        total = 0

        for num in nums:
            total += num
            prefix_remainder.append(total % k)

        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1

        for remainder in prefix_remainder:
            remainder_counts[remainder] += 1

            if remainder_counts[remainder] > 1:
                result += remainder_counts[remainder] - 1

        return result



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  96.40%
# Memory:   87.58%

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0

        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1

        total = 0

        for num in nums:
            total += num
            remainder = total % k

            remainder_counts[remainder] += 1

            if remainder_counts[remainder] > 1:
                result += remainder_counts[remainder] - 1

        return result
