#------------------------------------------------------
# Solution 1 - stack
#------------------------------------------------------

# Runtime:  86.37%
# Memory:   16.17%


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # push = append
        # pop  = pop(-1)

        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if not stack:
                    return False

                if c == "}" and stack[-1] == "{":
                    stack.pop(-1)
                elif c == "]" and stack[-1] == "[":
                    stack.pop(-1)
                elif c == ")" and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False

        return stack == []



#------------------------------------------------------
# Solution 2 - stack
#------------------------------------------------------

# Runtime:  86.37%
# Memory:   58.50%


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if not stack:
                    return False

                complement = stack.pop(-1)

                if c == "}" and complement == "{":
                    continue
                elif c == "]" and complement == "[":
                    continue
                elif c == ")" and complement == "(":
                    continue
                else:
                    return False

        return stack == []