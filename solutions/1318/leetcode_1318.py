#------------------------------------------------------
# Solution 1 - bit masking
#------------------------------------------------------

# Runtime:   6.59%
# Memory:   25.27%


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0

        mask = 1

        remaining_a = a
        remaining_b = b
        remaining_c = c

        while (remaining_a | remaining_b) != remaining_c:
            if remaining_c & mask == 0:
                if remaining_a & mask != 0:
                    result += 1
                
                if remaining_b & mask != 0:
                    result += 1

            if remaining_c & mask == 1:
                if (remaining_a | remaining_b) & mask != 1:
                    result += 1

            remaining_a = remaining_a >> 1
            remaining_b = remaining_b >> 1
            remaining_c = remaining_c >> 1

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 (optimized)
#------------------------------------------------------

# Runtime:  59.78%
# Memory:   68.57%


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0

        mask = 1

        remaining_a = a
        remaining_b = b
        remaining_c = c

        while (remaining_a | remaining_b) != remaining_c:
            if remaining_c & mask == 0:
                if remaining_a & mask != 0: result += 1
                if remaining_b & mask != 0: result += 1
            else:
                if (remaining_a | remaining_b) & mask != 1:
                    result += 1

            remaining_a = remaining_a >> 1
            remaining_b = remaining_b >> 1
            remaining_c = remaining_c >> 1

        return result



#------------------------------------------------------
# Solution 3 - xor
#------------------------------------------------------

# Runtime:   6.59%
# Memory:   68.57%


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0

        flip_count_01 = (a | b) ^ c
        flip_count_02 = (a & b) & ~c

        mask = 1

        while flip_count_01 or flip_count_02:
            result += flip_count_01 & mask
            result += flip_count_02 & mask

            flip_count_01 >>= 1
            flip_count_02 >>= 1

        return result