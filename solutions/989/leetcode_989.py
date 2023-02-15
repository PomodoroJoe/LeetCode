#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  77.55%
# Memory:   69.15%

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []

        index = len(num) - 1
        k_remaining = k
        carry = 0

        while k_remaining > 0 or index >= 0 or carry:
            k_ones = k_remaining % 10   # modulo
            num_val = num[index] if index >= 0 else 0

            val = k_ones + num_val + carry

            carry = 0
            
            if val >= 10:
                val = val % 10
                carry = 1

            result.append(val)

            k_remaining = k_remaining // 10
            index -= 1

        result = result[::-1]
        return result



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  80.44%
# Memory:   36.53%


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []

        index = len(num) - 1
        k_remaining = k
        carry = 0

        while k_remaining > 0 or index >= 0:
            k_ones = k_remaining % 10
            num_val = num[index] if index >= 0 else 0

            val = k_ones + num_val + carry

            carry = 0

            if val >= 10:
                val = val % 10
                carry = 1

            result.append(val)

            k_remaining = k_remaining // 10
            index -= 1

        if carry == 1:
            result.append(1)

        result = result[::-1]
        return result



#------------------------------------------------------
# Solution 3
#------------------------------------------------------

# Runtime:  84.65%
# Memory:   36.53%

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []

        i = len(num) - 1
        r = k
        c = 0

        while r > 0 or i >= 0:
            o = r % 10
            n = num[i] if i >= 0 else 0

            v = o + n + c

            c = 0

            if v >= 10:
                v = v % 10
                c = 1

            res.append(v)

            r = r // 10
            i -= 1

        if c == 1:
            res.append(1)

        res = res[::-1]
        return res


#------------------------------------------------------
# Solution 4
#------------------------------------------------------

# Runtime:  88.96%
# Memory:   11.71%


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []

        i = len(num) - 1
        r = k
        c = 0

        while r > 0 or i >= 0:
            o = r % 10
            r = r // 10

            n = num[i] if i >= 0 else 0
            i -= 1

            v = o + n + c

            c = 0

            if v >= 10:
                v = v % 10
                c = 1

            res.append(v)

        if c == 1:
            res.append(1)

        res = res[::-1]
        return res


#------------------------------------------------------
# Solution 5
#------------------------------------------------------

# Runtime:  87.19%
# Memory:   36.53%


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []

        i = len(num) - 1
        r = k
        c = 0

        while r > 0 or i >= 0:
            o = r % 10
            r = r // 10

            n = num[i] if i >= 0 else 0
            i -= 1

            v = o + n + c

            c = 0

            if v >= 10:
                v = v % 10
                c = 1

            res.append(v)

        if c == 1:
            res.append(1)

        res = res[::-1]
        return res



#------------------------------------------------------
# Solution 6
#------------------------------------------------------

# Runtime:  95.33%
# Memory:   36.53%


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []

        i = len(num) - 1
        r = k
        c = 0
        v = 0

        while r > 0 or i >= 0 or c:
            o = r % 10
            r = r // 10

            n = num[i] if i >= 0 else 0
            i -= 1

            v = o + n + c

            c = 0

            if v >= 10:
                v = v % 10
                c = 1

            res.append(v)

        res = res[::-1]
        return res