#------------------------------------------------------
# Solution 1 - bit mask
#------------------------------------------------------

# Runtime:  14.99%
# Memory:   63.69%


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        def CountOnes(num):
            count = 0

            # 0 0 = 0
            # 0 1 = 0
            # 1 0 = 0
            # 1 1 = 1

            while num:
                bit = num & 1 # mask = 00000000000000000000000000000001
                num = num >> 1
                count += bit

            return count


        for number in range(n + 1):
            ones_count = CountOnes(number)
            result.append(ones_count)

        return result


#------------------------------------------------------
# Solution 2 - Solution 1 w/o helper function
#------------------------------------------------------

# Runtime:  15.25%
# Memory:   94.10%


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for number in range(n + 1):
            ones_count = 0

            while number:
                bit = number & 1
                number = number >> 1
                ones_count += bit

            result.append(ones_count)

        return result