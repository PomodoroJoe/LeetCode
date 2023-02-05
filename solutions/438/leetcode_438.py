#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  68.53%
# Memory:   26.74%


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        result = []

        fp_p = defaultdict(int)
        fp_w = defaultdict(int)

        for c in p:
            fp_p[c] += 1

        start_index = 0
        end_index = 0

        while end_index < len(s):
            c = s[end_index]
            fp_w[c] += 1

            if end_index < len(p) - 1:
                end_index += 1
                continue

            if fp_p == fp_w:
                result.append(start_index)

            end_index += 1

            c = s[start_index]
            fp_w[c] -= 1

            if fp_w[c] == 0:
                del fp_w[c]

            start_index += 1

        return result




#------------------------------------------------------
# Solution 2 - remove temp vars
#------------------------------------------------------

# Runtime:  71.82%
# Memory:   97.12%


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        result = []

        fp_p = defaultdict(int)
        fp_w = defaultdict(int)

        for c in p:
            fp_p[c] += 1

        start_index = 0
        end_index = 0

        while end_index < len(s):
            fp_w[s[end_index]] += 1

            if end_index < len(p) - 1:
                end_index += 1
                continue

            if fp_p == fp_w:
                result.append(start_index)

            end_index += 1

            fp_w[s[start_index]] -= 1

            if fp_w[s[start_index]] == 0:
                del fp_w[s[start_index]]

            start_index += 1

        return result




#------------------------------------------------------
# Solution 3 - cache len(p)
#------------------------------------------------------

# Runtime:  78.21%
# Memory:   99.74%


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)

        if len(s) < len_p:
            return []

        result = []

        fp_p = defaultdict(int)
        fp_w = defaultdict(int)

        for c in p:
            fp_p[c] += 1

        start_index = 0
        end_index = 0

        while end_index < len(s):
            fp_w[s[end_index]] += 1

            if end_index < len_p - 1:
                end_index += 1
                continue

            if fp_p == fp_w:
                result.append(start_index)

            end_index += 1

            fp_w[s[start_index]] -= 1

            if fp_w[s[start_index]] == 0:
                del fp_w[s[start_index]]

            start_index += 1

        return result
