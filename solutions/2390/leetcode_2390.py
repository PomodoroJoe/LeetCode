#------------------------------------------------------
# Solution 1 - stack
#------------------------------------------------------

# Runtime:  63.13%
# Memory:   40.90%


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "*":
                stack.pop(-1)
            else:
                stack.append(c)

        return "".join(stack)




#------------------------------------------------------
# Solution 2 - duque
#------------------------------------------------------

# Runtime:  90.21%
# Memory:   14.29%


class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)




#------------------------------------------------------
# Solution 3 - duque w/ continue
#------------------------------------------------------

# Runtime:  95.16%
# Memory:   77.42%


class Solution:
    def removeStars(self, s: str) -> str:
        r = deque()

        for c in s:
            if c == "*":
                r.pop()
                continue
            r.append(c)

        return "".join(r)