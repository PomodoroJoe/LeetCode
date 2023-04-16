#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


from functools import cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        result = 0

        word_len = len(words[0])
        target_len = len(target)

        grid = [[0] * 26 for _ in range(word_len)]

        @cache
        def index_for_char(c):
            return ord(c) - ord('a')

        for i in range(word_len):
            for word in words:
                char_index = index_for_char(word[i])
                grid[i][char_index] += 1

        @cache
        def numWaysRecurse(start_index, target_index):
            result = 0

            if start_index >= word_len:
                return 0

            if target_index >= target_len:
                return 0

            target_char = target[target_index]
            target_char_index = index_for_char(target_char)

            for i in range(start_index, word_len):
                target_char_count = grid[i][target_char_index]

                if target_index < target_len - 1:
                    result += target_char_count * numWaysRecurse(i + 1, target_index + 1)
                else:
                    result += target_char_count

            return result


        result = numWaysRecurse(0, 0)
        return result % (pow(10, 9) + 7)




#------------------------------------------------------
# Solution 2 - Solution 1 w/ end_index
#------------------------------------------------------

# Runtime:   5.90%
# Memory:   45.88%


from functools import cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        result = 0

        word_len = len(words[0])
        target_len = len(target)

        grid = [[0] * 26 for _ in range(word_len)]

        @cache
        def index_for_char(c):
            return ord(c) - ord('a')

        for i in range(word_len):
            for word in words:
                char_index = index_for_char(word[i])
                grid[i][char_index] += 1

        @cache
        def numWaysRecurse(start_index, target_index):
            result = 0

            target_chars_remaining = target_len - target_index
            if target_chars_remaining <= 0:
                return 1

            if start_index >= word_len:
                return 0

            if target_index >= target_len:
                return 0

            target_char = target[target_index]
            target_char_index = index_for_char(target_char)

            end_index = max(start_index, word_len - target_chars_remaining)

            for i in range(start_index, end_index + 1):
                target_char_count = grid[i][target_char_index]

                if target_index < target_len - 1:
                    result += target_char_count * numWaysRecurse(i + 1, target_index + 1)
                else:
                    result += target_char_count

            return result


        result = numWaysRecurse(0, 0)
        return result % (pow(10, 9) + 7)