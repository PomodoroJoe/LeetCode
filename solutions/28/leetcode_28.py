#------------------------------------------------------
# Solution 1 - helper function
#------------------------------------------------------

# Runtime:  47.92%
# Memory:   11.30%


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1

        def isNeedle(i):
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    return False
            return True

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if isNeedle(i):
                    return i

        return result



#------------------------------------------------------
# Solution 2 - inline check
#------------------------------------------------------

# Runtime:  18.20%
# Memory:   95.82%


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:

                isNeedle = True
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j]:
                        isNeedle = False
                
                if isNeedle:
                    return i

        return result


#------------------------------------------------------
# Solution 3 - inline check with break
#------------------------------------------------------

# Runtime:  66.81%
# Memory:   11.30%


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:

                isNeedle = True
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j]:
                        isNeedle = False
                        break
                
                if isNeedle:
                    return i

        return -1



#------------------------------------------------------
# Solution 4 - continue
#------------------------------------------------------

# Runtime:  94.61%
# Memory:   95.82%


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] != needle[0]:
                continue

            isNeedle = True
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    isNeedle = False
                    break
            
            if isNeedle:
                return i

        return -1


#------------------------------------------------------
# Solution 5 - continue w/ cached needle len
#------------------------------------------------------

# Runtime:  97.85%
# Memory:   11.30%


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)

        for i in range(len(haystack) - needle_len + 1):
            if haystack[i] != needle[0]:
                continue

            isNeedle = True
            for j in range(needle_len):
                if needle[j] != haystack[i + j]:
                    isNeedle = False
                    break
            
            if isNeedle:
                return i

        return -1


#------------------------------------------------------
# Solution 6 - one line
#------------------------------------------------------

# Runtime:  90.82%
# Memory:   11.30%


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)