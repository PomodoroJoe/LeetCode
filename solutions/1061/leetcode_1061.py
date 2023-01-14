#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  98.86%
# Memory:   22.29%


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        result = ""

        # character -> smallest_character
        # key = character and value = smallest charcter in that group
        groups = {}

        def group(a, b):
            group_a = find_group(a)
            group_b = find_group(b)

            if group_a < group_b:
                groups[group_b] = group_a
            else:
                groups[group_a] = group_b


        def find_group(c):
            if c not in groups:
                groups[c] = c

            group_identifier = groups[c]

            if group_identifier == c:
                return c

            group_identifier = find_group(group_identifier)
            return group_identifier


        # groups
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]

            group(c1, c2)

        # build result
        for c in baseStr:
            result += find_group(c)

        return result


#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  93.71%
# Memory:   57.14%

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        result = ""

        # character -> smallest_character
        # key = character and value = smallest charcter in that group
        groups = {}

        def group(a, b):
            group_a = find_group(a)
            group_b = find_group(b)

            if group_a < group_b:
                groups[group_b] = group_a
            else:
                groups[group_a] = group_b


        def find_group(c):
            if c not in groups:
                groups[c] = c

            if groups[c] == c:
                return c

            groups[c] = find_group(groups[c])
            return groups[c]


        # groups
        for i in range(len(s1)):
            group(s1[i], s2[i])

        # build result
        for c in baseStr:
            result += find_group(c)

        return result
