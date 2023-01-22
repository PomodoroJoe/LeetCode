#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  45.57%
# Memory:   83.36%

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        if len(s) == 1:
            return [[s]]

        def isPalindrome(p):
            return p == p[::-1]

        if s and isPalindrome(s):
            result.append([s])

        for index in range(len(s)):
            first = s[:index + 1]
            
            if not isPalindrome(first):
                continue

            remaining_palindromes = self.partition(s[index + 1:])
            for remaining_palindrome in remaining_palindromes:
                result.append([first] + remaining_palindrome)

        return result


#------------------------------------------------------
# Solution 2 - w/ cache
#------------------------------------------------------

# Runtime:   5.49%
# Memory:    8.27%


from functools import cache

class Solution:

    @cache
    def partition(self, s: str) -> List[List[str]]:
        result = []

        if len(s) == 1:
            return [[s]]

        @cache
        def isPalindrome(p):
            return p == p[::-1]

        if s and isPalindrome(s):
            result.append([s])

        for index in range(len(s)):
            first = s[:index + 1]
            
            if not isPalindrome(first):
                continue

            remaining_palindromes = self.partition(s[index + 1:])
            for remaining_palindrome in remaining_palindromes:
                result.append([first] + remaining_palindrome)

        return result

