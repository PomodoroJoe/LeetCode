#------------------------------------------------------
# Solution 1 - stack
#------------------------------------------------------

# Runtime:   8.79%
# Memory:   28.25%


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        name = ""

        for c in path:
            if c != '/':
                name += c
            else:
                if name == ".":
                    name = ""
                elif name == "..":
                    if stack:
                        stack.pop(-1)
                    name = ""
                elif name != "":
                    stack.append(name)
                    name = ""

        if name == ".":
            name = ""
        elif name == "..":
            if stack:
                stack.pop(-1)
            name = ""
        elif name != "":
            stack.append(name)
            name = ""

        result = ""
        for name in stack:
            result += "/" + name

        return result if result else "/"



#------------------------------------------------------
# Solution 2 - stack DRY
#------------------------------------------------------

# Runtime:  21.51%
# Memory:   28.25%


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        name = ""

        for c in (path + "/"):
            if c != '/':
                name += c
            else:
                if name == ".":
                    name = ""
                elif name == "..":
                    if stack:
                        stack.pop(-1)
                    name = ""
                elif name != "":
                    stack.append(name)
                    name = ""

        result = ""
        for name in stack:
            result += "/" + name

        return result if result else "/"



#------------------------------------------------------
# Solution 4 - stack w/ join
#------------------------------------------------------

# Runtime:  66.29%
# Memory:   99.95%


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        name = ""

        for c in (path + "/"):
            if c != '/':
                name += c
            else:
                if name == ".":
                    pass
                elif name == "..":
                    if stack:
                        stack.pop(-1)
                elif name != "":
                    stack.append(name)
                name = ""

        result = "/" + "/".join(stack)
        return result



#------------------------------------------------------
# Solution 5 - Solution 4 w/ continue
#------------------------------------------------------

# Runtime:  86.71%
# Memory:   69.41%


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        name = ""

        for c in (path + "/"):
            if c != '/':
                name += c
            else:
                if not name or name == ".":
                    name = ""
                    continue
               
                if name == "..":
                    if stack:
                        stack.pop(-1)
                    name = ""
                else:
                    stack.append(name)
                    name = ""

        result = "/" + "/".join(stack)
        return result



#------------------------------------------------------
# Solution 8 - Solution 5 w/ minimized names
#------------------------------------------------------

# Runtime:  90.20%
# Memory:   97.52%


class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        e = path.split("/")

        for n in e:
            if not n or n == ".": continue
            if n == "..":
                if s: s.pop(-1)
            else: s.append(n)

        r = "/" + "/".join(s)
        return r


#------------------------------------------------------
# Solution 9 - Solution 8 w/0 empty lines
#------------------------------------------------------

# Runtime:  94.52%
# Memory:   28.25%


class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        e = path.split("/")
        for n in e:
            if not n or n == ".": continue
            if n == "..":
                if s: s.pop(-1)
            else: s.append(n)
        r = "/" + "/".join(s)
        return r