#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  95.82%
# Memory:   18.45%


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""

        a_index = len(a) - 1
        b_index = len(b) - 1
        carry = 0

        while a_index >= 0 or b_index >= 0:

            a_val = a[a_index] if a_index >= 0 else "0"
            b_val = b[b_index] if b_index >= 0 else "0"

            if a_val == "0" and b_val == "0" and carry == 0:
                result += "0"

            elif a_val == "1" and b_val == "0" and carry == 0:
                result += "1"

            elif a_val == "0" and b_val == "1" and carry == 0:
                result += "1"

            elif a_val == "1" and b_val == "1" and carry == 0:
                result += "0"
                carry = 1


            elif a_val == "0" and b_val == "0" and carry == 1:
                result += "1"
                carry = 0

            elif a_val == "1" and b_val == "0" and carry == 1:
                result += "0"

            elif a_val == "0" and b_val == "1" and carry == 1:
                result += "0"

            elif a_val == "1" and b_val == "1" and carry == 1:
                result += "1"

            a_index -= 1
            b_index -= 1

        if carry == 1:
            result += "1"

        result = result[::-1]
        return result