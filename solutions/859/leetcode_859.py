#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  94.59%
# Memory:   92.40%


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        len_s = len(s)
        len_g = len(goal)

        if len_s != len_g:
            return False

        mismatched_index_1 = None
        mismatched_index_2 = None

        has_duplicate = False

        letters = set()

        for index in range(len_s):
            letter_s = s[index]
            letter_g = goal[index]

            if letter_s in letters:
                has_duplicate = True

            letters.add(letter_s)

            if letter_s != letter_g:
                if mismatched_index_1 == None:
                    mismatched_index_1 = index
                    continue

                if mismatched_index_2 == None:
                    mismatched_index_2 = index
                    continue

                return False

        if mismatched_index_1 == None and mismatched_index_2 == None:
            return has_duplicate

        if mismatched_index_1 != None and mismatched_index_2 == None:
            return False

        return s[mismatched_index_1] == goal[mismatched_index_2] and \
               s[mismatched_index_2] == goal[mismatched_index_1]