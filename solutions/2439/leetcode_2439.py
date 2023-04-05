#------------------------------------------------------
# Solution 1 - running average
#------------------------------------------------------

# Runtime:  73.90%
# Memory:   84.30%


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]

        total = nums[0]
        for index in range(1, len(nums)):
            total += nums[index]
            per_cell_value = ceil(total / (index + 1))

            result = max(result, per_cell_value)

        return result



#------------------------------------------------------
# Solution 2 - water chamber approach w/ overflow
#------------------------------------------------------

# Runtime:  90.13%
# Memory:   39.46%


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]

        capacity = 0

        for i in range(len(nums)):
            current_val = nums[i]

            if current_val <= result:
                capacity += result - current_val
                continue

            cell_overflow = current_val - result
            if cell_overflow <= capacity:
                capacity -= cell_overflow
            else:
                total_overflow = cell_overflow - capacity
                spread = ceil(total_overflow / (i + 1))
                result += spread
                capacity = (spread * (i + 1)) - total_overflow

        return result


#------------------------------------------------------
# Solution 3 - water chamber approach (minified)
#------------------------------------------------------

# Runtime:  92.83%
# Memory:   39.46%


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        r = nums[0]

        c = 0

        for i in range(len(nums)):
            cv = nums[i]

            if cv <= r:
                c += r - cv
                continue

            co = cv - r
            if co <= c:
                c -= co
            else:
                to = co - c
                s = ceil(to / (i + 1))
                r += s
                c = (s * (i + 1)) - to

        return r
