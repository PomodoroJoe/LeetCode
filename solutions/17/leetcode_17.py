#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  81.43%
# Memory:   86.50%


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letter_map = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        def letterCombinationsRecurse(remaining_digits):
            if remaining_digits == "":
                return []

            if len(remaining_digits) == 1:
                digit = remaining_digits[0]
                letters = digit_to_letter_map[digit]

                result = []
                for c in letters:
                    result.append(c)
                return result

            digit = remaining_digits[0]
            letters = digit_to_letter_map[digit]

            result = []

            for c in letters:
                prefix = c

                suffixes = letterCombinationsRecurse(remaining_digits[1:])
                for suffix in suffixes:
                    option = prefix + suffix
                    result.append(option)

            return result

        return letterCombinationsRecurse(digits)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  68.89%
# Memory:   19.66%


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letter_map = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        @cache
        def letterCombinationsRecurse(remaining_digits):
            if remaining_digits == "":
                return []

            if len(remaining_digits) == 1:
                digit = remaining_digits[0]
                letters = digit_to_letter_map[digit]

                result = []
                for c in letters:
                    result.append(c)
                return result

            digit = remaining_digits[0]
            letters = digit_to_letter_map[digit]

            result = []

            for c in letters:
                prefix = c

                suffixes = letterCombinationsRecurse(remaining_digits[1:])
                for suffix in suffixes:
                    option = prefix + suffix
                    result.append(option)

            return result

        return letterCombinationsRecurse(digits)



#------------------------------------------------------
# Solution 3 - Solution 1 w/o helper vars
#------------------------------------------------------

# Runtime:  88.35%
# Memory:   57.40%


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letter_map = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        def letterCombinationsRecurse(remaining_digits):
            if remaining_digits == "":
                return []

            if len(remaining_digits) == 1:
                digit = remaining_digits[0]
                letters = digit_to_letter_map[digit]

                result = []
                for c in letters:
                    result.append(c)
                return result

            digit = remaining_digits[0]
            letters = digit_to_letter_map[digit]

            result = []

            for c in letters:
                suffixes = letterCombinationsRecurse(remaining_digits[1:])
                for suffix in suffixes:
                    option = c + suffix
                    result.append(option)

            return result

        return letterCombinationsRecurse(digits)



#------------------------------------------------------
# Solution 4 - Solution 3 w/ mapping on one line
#------------------------------------------------------

# Runtime:  98.78%
# Memory:   19.68%


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letter_map = { '2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz" }

        def letterCombinationsRecurse(remaining_digits):
            if remaining_digits == "":
                return []

            if len(remaining_digits) == 1:
                digit = remaining_digits[0]
                letters = digit_to_letter_map[digit]

                result = []
                for c in letters:
                    result.append(c)
                return result

            digit = remaining_digits[0]
            letters = digit_to_letter_map[digit]

            result = []

            for c in letters:
                suffixes = letterCombinationsRecurse(remaining_digits[1:])
                for suffix in suffixes:
                    option = c + suffix
                    result.append(option)

            return result

        return letterCombinationsRecurse(digits)


#------------------------------------------------------
# Solution 6 - Solution 4 w/ array map
#------------------------------------------------------

# Runtime:  90.28%
# Memory:   99.92%


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letter_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def letterCombinationsRecurse(remaining_digits):
            if remaining_digits == "":
                return []

            digit = int(remaining_digits[0]) - 2
            letters = digit_to_letter_map[digit]

            if len(remaining_digits) == 1:
                result = []
                for c in letters:
                    result.append(c)
                return result

            result = []

            for c in letters:
                suffixes = letterCombinationsRecurse(remaining_digits[1:])
                for suffix in suffixes:
                    option = c + suffix
                    result.append(option)

            return result

        return letterCombinationsRecurse(digits)