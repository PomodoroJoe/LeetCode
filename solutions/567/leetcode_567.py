#------------------------------------------------------
# Solution 1 - permutations
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for permutation in permutations(s1, len(s1)):
            if ''.join(permutation) in s2:
                return True

        return False



#------------------------------------------------------
# Solution 2 - array
#------------------------------------------------------

# Runtime:  94.41%
# Memory:   28.45%


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_1 = [0] * 26
        count_2 = [0] * 26

        base = ord('a')

        for c in s1:
            i = ord(c) - base
            count_1[i] += 1

        start_index = 0
        end_index = 0

        while end_index < len(s1) - 1:
            c = s2[end_index]

            i = ord(c) - base
            count_2[i] += 1

            end_index += 1

        
        while end_index < len(s2):
            c = s2[end_index]

            i = ord(c) - base
            count_2[i] += 1

            if count_2 == count_1:
                return True

            start_c = s2[start_index]
            i = ord(start_c) - base
            count_2[i] -= 1

            end_index += 1
            start_index += 1

        return False



#------------------------------------------------------
# Solution 3 - defaultdict
#------------------------------------------------------

# Runtime:  91.44%
# Memory:   64.59%


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_1 = defaultdict(int)
        count_2 = defaultdict(int)

        base = ord('a')

        for c in s1:
            i = ord(c) - base
            count_1[i] += 1

        start_index = 0
        end_index = 0

        while end_index < len(s1) - 1:
            c = s2[end_index]

            i = ord(c) - base
            count_2[i] += 1

            end_index += 1

        
        while end_index < len(s2):
            c = s2[end_index]

            i = ord(c) - base
            count_2[i] += 1

            if count_2 == count_1:
                return True

            start_c = s2[start_index]
            i = ord(start_c) - base
            count_2[i] -= 1

            if count_2[i] == 0:
                del count_2[i]

            end_index += 1
            start_index += 1

        return False