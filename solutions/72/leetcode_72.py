#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        result = 0

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:],  word2[1:])
        else:
            #insert
            option1 = 1 + self.minDistance(word1,  word2[1:])

            # delete
            option2 = 1 + self.minDistance(word1[1:],  word2)

            # replace
            option3 = 1 + self.minDistance(word1[1:],  word2[1:])

            result = min(option1, option2, option3)

        return result



#------------------------------------------------------
# Solution 2 - recursive w/ cache
#------------------------------------------------------

# Runtime:  77.81%
# Memory:   05.10%


from functools import cache

class Solution:

    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        result = 0

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:],  word2[1:])
        else:
            #insert
            option1 = 1 + self.minDistance(word1,  word2[1:])

            # delete
            option2 = 1 + self.minDistance(word1[1:],  word2)

            # replace
            option3 = 1 + self.minDistance(word1[1:],  word2[1:])

            result = min(option1, option2, option3)

        return result



#------------------------------------------------------
# Solution 3 - recursive w/ cache & while loop for prefix
#------------------------------------------------------

# Runtime:  26.31%
# Memory:   05.10%


from functools import cache

class Solution:

    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        result = 0

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        index = 0
        max_index = min(len(word1), len(word2))

        while index < max_index and word1[index] == word2[index]:
            index += 1

        new_word1 = word1[index:] if index < len(word1) else ""
        new_word2 = word2[index:] if index < len(word2) else ""

        if new_word1 == "":
            return len(new_word2)

        if new_word2 == "":
            return len(new_word1)

        if new_word1[0] != new_word2[0]:
            #insert
            option1 = 1 + self.minDistance(word1[index:],  word2[index+1:])

            # delete
            option2 = 1 + self.minDistance(word1[index+1:],  word2[index:])

            # replace
            option3 = 1 + self.minDistance(word1[index+1:],  word2[index+1:])

            result = min(option1, option2, option3)

        return result


#------------------------------------------------------
# Solution 4 - recursive w/ cache & change of order
#------------------------------------------------------

# Runtime:  79.51%
# Memory:   05.10%



from functools import cache

class Solution:

    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        result = 0

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        if word1[0] != word2[0]:
            #insert
            option1 = 1 + self.minDistance(word1,  word2[1:])

            # delete
            option2 = 1 + self.minDistance(word1[1:],  word2)

            # replace
            option3 = 1 + self.minDistance(word1[1:],  word2[1:])

            return min(option1, option2, option3)

        return self.minDistance(word1[1:],  word2[1:])



#------------------------------------------------------
# Solution 5 - recursive w/ dynamic programming
#------------------------------------------------------

# Runtime:  92.13%
# Memory:   07.71%


class Solution:

    dp = {}

    def minDistance(self, word1: str, word2: str) -> int:
        key = (word1, word2)
        if key in self.dp:
            return self.dp[key]

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        if word1[0] != word2[0]:
            #insert
            option1 = 1 + self.minDistance(word1,  word2[1:])

            # delete
            option2 = 1 + self.minDistance(word1[1:],  word2)

            # replace
            option3 = 1 + self.minDistance(word1[1:],  word2[1:])

            self.dp[key] = min(option1, option2, option3)
            return self.dp[key]

        self.dp[key] = self.minDistance(word1[1:],  word2[1:])
        return self.dp[key]