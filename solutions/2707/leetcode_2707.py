#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  95.63%
# Memory:   49.40%


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        # key = start char, value = list of words that start with start char
        word_map = defaultdict(list)
        for word in dictionary:
            word_map[word[0]].append(word)

        @cache
        def minExtraCharRecurse(start_index):
            if start_index >= len(s):
                return 0

            result = inf
            start_char = s[start_index]

            for word in word_map[start_char]:
                end_index = start_index + len(word)
                if word == s[start_index:end_index]:
                    option = minExtraCharRecurse(end_index)
                    result = min(result, option)

            alternative = 1 + minExtraCharRecurse(start_index + 1)

            return result if result < alternative else alternative

        return minExtraCharRecurse(0)