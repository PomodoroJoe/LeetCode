#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  66.14%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        x_index = 0
        y_index = n

        while y_index < len(nums):
            result.append(nums[x_index])
            result.append(nums[y_index])

            x_index += 1
            y_index += 1

        return result



#------------------------------------------------------
# Solution 2 - max_index
#------------------------------------------------------

# Runtime:  59.91%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        x_index = 0
        y_index = n

        max_index = 2 * n

        while y_index < max_index:
            result.append(nums[x_index])
            result.append(nums[y_index])

            x_index += 1
            y_index += 1

        return result



#------------------------------------------------------
# Solution 3 - +=
#------------------------------------------------------

# Runtime:  59.91%
# Memory:   86.25%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        x_index = 0
        y_index = n

        while y_index < len(nums):
            result += [nums[x_index]]
            result += [nums[y_index]]

            x_index += 1
            y_index += 1

        return result


#------------------------------------------------------
# Solution 4
#------------------------------------------------------

# Runtime:  79.90%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        x_index = 0
        y_index = n

        while y_index < len(nums):
            result += [nums[x_index], nums[y_index]]

            x_index += 1
            y_index += 1

        return result


#------------------------------------------------------
# Solution 5 - what?
#------------------------------------------------------

# Runtime:  33.41%
# Memory:   86.25%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        index = 0

        while index < n:
            result += [nums[index], nums[index + n]]
            index += 1


        return result


#------------------------------------------------------
# Solution 6
#------------------------------------------------------

# Runtime:  79.90%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        index = n

        while index < len(nums):
            result += [nums[index - n], nums[index]]
            index += 1


        return result



#------------------------------------------------------
# Solution 7
#------------------------------------------------------

# Runtime:  86.74%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        index = n

        while index < len(nums):
            result += [nums[index - n]]
            result += [nums[index]]
            index += 1


        return result



#------------------------------------------------------
# Solution 8 - Winner!
#------------------------------------------------------

# Runtime:  99.85%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        index = 0

        while index < n:
            result += [nums[index]]
            result += [nums[index + n]]
            index += 1


        return result



#------------------------------------------------------
# Solution 9 - whitespace?  Srsly?
#------------------------------------------------------

# Runtime:  66.14%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        index = 0

        while index < n:
            result += [nums[index]]
            result += [nums[index + n]]
            index += 1

        return result



#------------------------------------------------------
# Solution 10 - I'm suspicious of these numbers...
#------------------------------------------------------

# Runtime:  98.97%
# Memory:   33.41%


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        index = 0

        while index < n:
            result += [nums[index]]
            result += [nums[index + n]]
            index += 1


        return result