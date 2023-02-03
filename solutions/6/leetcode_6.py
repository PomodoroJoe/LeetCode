
#------------------------------------------------------
# Solution 1 - zigzag x & y
#------------------------------------------------------

# Runtime:  47.78%
# Memory:   17.57%


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        x = 0
        y = 0

        down = True

        element_array = []

        for c in s:
            element = (x, y, c)
            element_array.append(element)

            if down:
                y += 1
            else:
                y -= 1
                x += 1

            if y < 0:
                down = True
                y = 1

            if y == numRows:
                down = False
                y -= 2

        element_array.sort(key = lambda x: (x[1], x[0]))

        result = ""
        for element in element_array:
            result += element[2]

        return result


#------------------------------------------------------
# Solution 2 - added early return condition
#------------------------------------------------------

# Runtime:  48.77%
# Memory:   29.22%


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s

        x = 0
        y = 0

        down = True

        element_array = []

        for c in s:
            element = (x, y, c)
            element_array.append(element)

            if down:
                y += 1
            else:
                y -= 1
                x += 1

            if y < 0:
                down = True
                y = 1

            if y == numRows:
                down = False
                y -= 2

        element_array.sort(key = lambda x: (x[1], x[0]))

        result = ""
        for element in element_array:
            result += element[2]

        return result




#------------------------------------------------------
# Solution 3 - zigzag y only (x implied w/ append)
#------------------------------------------------------

# Runtime:  61.60%
# Memory:   29.22%


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s

        y = 0
        down = True

        element_array = []

        for c in s:
            element = (y, c)
            element_array.append(element)

            if down:
                y += 1
            else:
                y -= 1

            if y < 0:
                down = True
                y = 1

            if y == numRows:
                down = False
                y -= 2

        element_array.sort(key = lambda x: (x[0]))

        result = ""
        for element in element_array:
            result += element[1]

        return result



#------------------------------------------------------
# Solution 4 - zigzag w/ y_step
#------------------------------------------------------

# Runtime:  89.23%
# Memory:   29.22%


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s

        y = 0
        y_step = 1

        element_array = []

        for c in s:
            element = (y, c)
            element_array.append(element)

            y += y_step

            if y < 0:
                y_step = 1
                y = 1

            if y == numRows:
                y_step = -1
                y -= 2

        element_array.sort(key = lambda x: (x[0]))

        result = ""
        for element in element_array:
            result += element[1]

        return result



#------------------------------------------------------
# Solution 5 - store rows (not elements)
#------------------------------------------------------

# Runtime:  74.18%
# Memory:   94.57%


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s

        y = 0
        y_step = 1

        rows = [""] * numRows

        for c in s:
            rows[y] += c

            y += y_step

            if y < 0:
                y_step = 1
                y = 1

            if y == numRows:
                y_step = -1
                y -= 2

        result = ""
        for row in rows:
            result += row

        return result



#------------------------------------------------------
# Solution 6 - use join to build result
#------------------------------------------------------

# Runtime:  81.12%
# Memory:   94.57%



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s

        y = 0
        y_step = 1

        rows = [""] * numRows

        for c in s:
            rows[y] += c

            y += y_step

            if y < 0:
                y_step = 1
                y = 1

            if y == numRows:
                y_step = -1
                y -= 2

        result = "".join(rows)
        return result