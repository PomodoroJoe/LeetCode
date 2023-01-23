#------------------------------------------------------
# Solution 1 - set & dictionary
#------------------------------------------------------

# Runtime:  38.47%
# Memory:   25.51%

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        result = -1

        # people who trust others
        trusting = set()

        # key = trusted person label, value set of all those who trust them
        trusted_by = defaultdict(set)

        for trust_connection in trust:
            truster = trust_connection[0]
            trusted = trust_connection[1]

            trusting.add(truster)
            trusted_by[trusted].add(truster)

        for i in range(1, n+1):
            if i in trusting:
                continue

            if len(trusted_by[i]) == n - 1:
                return i

        return result


#------------------------------------------------------
# Solution 2 - arrays
#------------------------------------------------------

# Runtime:  38.42%
# Memory:   90.33%


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        result = -1

        # people who trust others
        trusting = [0 for _ in range(n+1)]

        # key = trusted person label, value set of all those who trust them
        trusted_by = [0 for _ in range(n+1)]

        for trust_connection in trust:
            truster = trust_connection[0]
            trusted = trust_connection[1]

            trusting[truster] += 1
            trusted_by[trusted] += 1

        for i in range(1, n+1):
            if trusting[i] > 0:
                continue

            if trusted_by[i] == n - 1:
                return i

        return result



#------------------------------------------------------
# Solution 3 - arrays, short variable names, limit var
#------------------------------------------------------

# Runtime:  64.45%
# Memory:   59.70%

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        result = -1

        # people who trust others
        trusting = [0 for _ in range(n+1)]

        # key = trusted person label, value set of all those who trust them
        trusted_by = [0 for _ in range(n+1)]

        for t in trust:
            truster = t[0]
            trusted = t[1]

            trusting[truster] += 1
            trusted_by[trusted] += 1

        limit = n - 1
        for i in range(1, n+1):
            if trusting[i] != 0:
                continue

            if trusted_by[i] == limit:
                return i

        return result
