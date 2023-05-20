#------------------------------------------------------
# Solution 1 - recursive (dfs variation)
#------------------------------------------------------

# Runtime:  37.13%
# Memory:    8.81%


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # key = variable, value = dict: key = other variable, value = factor
        mapping = defaultdict(dict)

        for i, val in enumerate(values):
            a, b = equations[i]

            mapping[a][b] = val
            mapping[b][a] = 1 / val

            mapping[a][a] = 1
            mapping[b][b] = 1

        
        # c / d
        def calc(c, d, visited):
            if c not in mapping or d not in mapping:
                return -1

            if c == d:
                return 1

            result = -1
            visited.add(c)

            for k in mapping[c]:
                if k in mapping[d]:
                    val = mapping[c][k] / mapping[d][k]
                    return val
                else:
                    if k not in visited:
                        val = calc(k, d, visited)
                        result = val * mapping[c][k] if val != -1 else result

            return result


        results = []

        for q in queries:
            c, d = q
            result = calc(c, d, set())
            results.append(result)

        return results