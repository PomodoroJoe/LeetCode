#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  20.85%
# Memory:   47.98%


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        
        set_of_words = set(words)

        def isConcatenatedWord(word, isRecurse = True):
            if word in set_of_words and isRecurse:
                return True

            split_index = 1

            while split_index < len(word):
                left = word[:split_index]
                right = word[split_index:]

                if left in set_of_words and isConcatenatedWord(right):
                    return True

                split_index += 1

            return False


        for word in words:
            if isConcatenatedWord(word, False):
                result.append(word)

        return result



#------------------------------------------------------
# Solution 2 - recursive w/ cache
#------------------------------------------------------

# Runtime:  43.93%
# Memory:   34.94%


from functools import cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        
        set_of_words = set(words)

        @cache
        def isConcatenatedWord(word, isRecurse = True):
            if word in set_of_words and isRecurse:
                return True

            split_index = 1

            while split_index < len(word):
                left = word[:split_index]
                right = word[split_index:]

                if left in set_of_words and isConcatenatedWord(right):
                    return True

                split_index += 1

            return False


        for word in words:
            if isConcatenatedWord(word, False):
                result.append(word)

        return result



#------------------------------------------------------
# Solution 3 - recursive w/ cache & fewer temp vars
#------------------------------------------------------

# Runtime:  85.79%
# Memory:   34.94%


from functools import cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        
        set_of_words = set(words)

        @cache
        def isConcatenatedWord(word, isRecurse = True):
            if word in set_of_words and isRecurse:
                return True

            split_index = 1

            while split_index < len(word):
                if word[:split_index] in set_of_words and isConcatenatedWord(word[split_index:]):
                    return True

                split_index += 1

            return False


        for word in words:
            if isConcatenatedWord(word, False):
                result.append(word)

        return result
