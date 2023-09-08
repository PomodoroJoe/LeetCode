#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  30.77%
# Memory:   71.54%


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for row in range(1, numRows):
            new_row = [1]
            row_len = row
            prev_row = result[-1]

            for element in range(1, row_len):
                A = prev_row[element - 1]
                B = prev_row[element]
                new_row.append(A + B)
            new_row.append(1)

            result.append(new_row)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 (minified)
#------------------------------------------------------

# Runtime:  63.96%
# Memory:   71.54%


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for r in range(1, numRows):
            new_row = [1]
            prev_row = result[-1]

            for e in range(1, r):
                A = prev_row[e - 1]
                B = prev_row[e]
                new_row.append(A + B)
            new_row.append(1)

            result.append(new_row)

        return result



#------------------------------------------------------
# Solution 3 - Solution 2 (minified more)
#------------------------------------------------------

# Runtime:  84.10%
# Memory:   71.54%


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for r in range(1, numRows):
            new_row = [1]
            prev_row = result[-1]
            for e in range(1, r):
                A = prev_row[e - 1]
                B = prev_row[e]
                new_row.append(A + B)
            new_row.append(1)
            result.append(new_row)

        return result