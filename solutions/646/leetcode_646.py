#------------------------------------------------------
# Solution 1 - sort by right val
#------------------------------------------------------

# Runtime:  95.54%
# Memory:   14.24%


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        result = 0

        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        max_right = None

        for pair in sorted_pairs:
            if max_right == None:
                max_right = pair[1]
                result = 1
                continue

            if pair[0] > max_right:
                max_right = pair[1]
                result += 1

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ early out
#------------------------------------------------------

# Runtime:  94.74%
# Memory:   35.43%


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0

        result = 0

        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        max_right = sorted_pairs[0][1]
        result = 1

        for pair in sorted_pairs[1:]:
            if pair[0] > max_right:
                max_right = pair[1]
                result += 1

        return result



#------------------------------------------------------
# Solution 3 - Solution 2 (more compact)
#------------------------------------------------------

# Runtime:  96.79%
# Memory:   65.60%


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return 0

        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        max_right = sorted_pairs[0][1]
        result = 1

        for pair in sorted_pairs[1:]:
            if pair[0] > max_right:
                max_right = pair[1]
                result += 1

        return result