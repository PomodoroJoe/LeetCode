#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  51.38%
# Memory:   21.82%


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        for c in letters:
            if c > target:
                return c

        return letters[0]



#------------------------------------------------------
# Solution 2 - Solution 1 (minimized)
#------------------------------------------------------

# Runtime:  67.29%
# Memory:   67.25%


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target: return c
        return letters[0]