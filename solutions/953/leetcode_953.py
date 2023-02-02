
#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  68.77%
# Memory:   77.53%


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        character_map = {}

        for i, c in enumerate(order):
            character_map[c] = i


        # -1 = ASCENDING
        #  0 = SAME
        #  1 = DESCENDING

        def comparator(A, B):
            if A == B:
                return 0

            min_count = min(len(A), len(B))

            for i in range(min_count):
                i_A = character_map[A[i]]
                i_B = character_map[B[i]]

                if i_A < i_B:
                    return -1

                if i_A > i_B:
                    return 1

            if len(A) > len(B):
                return 1

            if len(A) < len(B):
                return -1

            return 0

        
        for i in range(1, len(words)):
            if comparator(words[i - 1], words[i]) == 1:
                return False

        return True



#------------------------------------------------------
# Solution 2 - store len() in variables
#------------------------------------------------------

# Runtime:  93.57%
# Memory:   77.53%


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        character_map = {}

        for i, c in enumerate(order):
            character_map[c] = i


        # -1 = ASCENDING
        #  0 = SAME
        #  1 = DESCENDING

        def comparator(A, B):
            if A == B:
                return 0

            len_A = len(A)
            len_B = len(B)

            min_count = min(len_A, len_B)

            for i in range(min_count):
                i_A = character_map[A[i]]
                i_B = character_map[B[i]]

                if i_A < i_B:
                    return -1

                if i_A > i_B:
                    return 1

            if len_A > len_B:
                return 1

            if len_A < len_B:
                return -1

            return 0

        
        for i in range(1, len(words)):
            if comparator(words[i - 1], words[i]) == 1:
                return False

        return True