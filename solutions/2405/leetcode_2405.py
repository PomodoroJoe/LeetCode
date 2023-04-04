#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def partitionString(self, s: str) -> int:
        result = 1

        seen_characters = set()

        for i in range(len(s)):
            if s[i] not in seen_characters:
                seen_characters.add(s[i])
            else:
                return 1 + self.partitionString(s[i:])

        return result



#------------------------------------------------------
# Solution 2 - iterative
#------------------------------------------------------

# Runtime:  39.28%
# Memory:   90.81%


class Solution:
    def partitionString(self, s: str) -> int:
        result = 1

        seen_characters = set()

        for i in range(len(s)):
            if s[i] not in seen_characters:
                seen_characters.add(s[i])
            else:
                #return 1 + self.partitionString(s[i:])
                result += 1
                seen_characters.clear()
                seen_characters.add(s[i])

        return result



#------------------------------------------------------
# Solution 3 - iterative w/o indexing
#------------------------------------------------------

# Runtime:  77.50%
# Memory:   47.27%


class Solution:
    def partitionString(self, s: str) -> int:
        result = 1

        seen_characters = set()

        for c in s:
            if c not in seen_characters:
                seen_characters.add(c)
            else:
                result += 1
                seen_characters.clear()
                seen_characters.add(c)

        return result


#------------------------------------------------------
# Solution 4 - iterative refactor
#------------------------------------------------------

# Runtime:  88.28%
# Memory:   47.27%


class Solution:
    def partitionString(self, s: str) -> int:
        result = 1

        seen_characters = set()

        for c in s:
            if c in seen_characters:
                result += 1
                seen_characters.clear()
            seen_characters.add(c)

        return result


#------------------------------------------------------
# Solution 5 - iterative new set
#------------------------------------------------------

# Runtime:  80.83%
# Memory:   47.27%


class Solution:
    def partitionString(self, s: str) -> int:
        result = 1

        seen_characters = set()

        for c in s:
            if c in seen_characters:
                result += 1
                seen_characters = set()
            seen_characters.add(c)

        return result


#------------------------------------------------------
# Solution 6 - iterative w/o set
#------------------------------------------------------

# Runtime:  94.27%
# Memory:   47.27%


lass Solution:
    def partitionString(self, s: str) -> int:
        result = 1

        seen_characters = ""

        for c in s:
            if c in seen_characters:
                result += 1
                seen_characters = ""
            seen_characters += c

        return result


#------------------------------------------------------
# Solution 7 - iterative w/ short names
#------------------------------------------------------

# Runtime:  98.80%
# Memory:   90.81%


class Solution:
    def partitionString(self, s: str) -> int:
        r = 1

        sc = ""

        for c in s:
            if c in sc:
                r += 1
                sc = ""
            sc += c

        return r