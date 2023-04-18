#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:   5.91%
# Memory:   55.13%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2

        if not word2:
            return word1

        result = word1[0] + word2[0]
        result += self.mergeAlternately(word1[1:], word2[1:])

        return result


#------------------------------------------------------
# Solution 2 - Solution 1 w/ optimizations
#------------------------------------------------------

# Runtime:  63.30%
# Memory:    9.46%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2

        if not word2:
            return word1

        return word1[0] + word2[0] + self.mergeAlternately(word1[1:], word2[1:])



#------------------------------------------------------
# Solution 3 - iterative
#------------------------------------------------------

# Runtime:   5.91%
# Memory:   55.13


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        word1_len = len(word1)
        word2_len = len(word2)

        max_len = max(word1_len, word2_len)

        for i in range(max_len):
            result += word1[i] if i < word1_len else ""
            result += word2[i] if i < word2_len else ""

        return result


#------------------------------------------------------
# Solution 4 - Solution 3 w/ different spacing
#------------------------------------------------------

# Runtime:  32.83%
# Memory:   55.13%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        word1_len = len(word1)
        word2_len = len(word2)

        max_len = word1_len if word1_len > word2_len else word2_len

        for i in range(max_len):
            result += word1[i] if i < word1_len else ""
            result += word2[i] if i < word2_len else ""

        return result



#------------------------------------------------------
# Solution 5 - Solution 3 w/o appending empty strings
#------------------------------------------------------

# Runtime:  14.51%
# Memory:   55.13%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        word1_len = len(word1)
        word2_len = len(word2)

        max_len = word1_len if word1_len > word2_len else word2_len

        for i in range(max_len):
            if i < word1_len:
                result += word1[i]

            if i < word2_len:
                result += word2[i]

        return result


#------------------------------------------------------
# Solution 6 - Solution 5 w/ different spacing
#------------------------------------------------------

# Runtime:  42.24%
# Memory:   95.97%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        word1_len = len(word1)
        word2_len = len(word2)

        max_len = word1_len if word1_len > word2_len else word2_len

        for i in range(max_len):
            if i < word1_len:
                result += word1[i]
            if i < word2_len:
                result += word2[i]

        return result


#------------------------------------------------------
# Solution 7 - Solution 5 w/ min_len
#------------------------------------------------------

# Runtime:  17.20%
# Memory:   95.97%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        word1_len = len(word1)
        word2_len = len(word2)

        min_len = word1_len if word1_len < word2_len else word2_len

        for i in range(min_len):
            result += word1[i] + word2[i]

        if word1_len > word2_len:
            result += word1[word2_len:]

        if word2_len > word1_len:
            result += word2[word1_len:]

        return result


#------------------------------------------------------
# Solution 8 - zip
#------------------------------------------------------

# Runtime:  72.43%
# Memory:    9.46%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        word1_len = len(word1)
        word2_len = len(word2)

        result = "".join(a + b for a, b in zip(word1, word2))

        if word1_len > word2_len:
            result += word1[word2_len:]

        if word2_len > word1_len:
            result += word2[word1_len:]

        return result