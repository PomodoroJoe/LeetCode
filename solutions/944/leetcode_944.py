#------------------------------------------------------
# Solution 1
#------------------------------------------------------

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0

        len_str = len(strs[0])
        string_count = len(strs)

        for i in range(len_str):
            for j in range(1, string_count):
                if strs[j][i] < strs[j-1][i]:
                    result += 1
                    break

        return result


#------------------------------------------------------
# Solution 2
#------------------------------------------------------

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        
        cols = zip(*strs)

        for col in cols:
            if sorted(col) != list(col):
                result += 1

        return result
