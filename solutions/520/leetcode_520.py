#------------------------------------------------------
# Solution 1
#------------------------------------------------------

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True

        first_letter_case = word[0].isupper()
        second_letter_case = word[1].isupper()

        if second_letter_case and not first_letter_case:
            return False

        for i in range(2, len(word)):
            if word[i].isupper() != second_letter_case:
                return False

        return True



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
