#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  69.44%
# Memory:   11.74%


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        nodes = defaultdict(set)

        for i, p in enumerate(parent):
            nodes[p].add(i)

        result = 0

        def longestPathRecurse(node):
            nonlocal result
            
            recurseResult = 1

            longestPathA = 0
            longestPathB = 0

            for connected_node in nodes[node]:
                longestPathForNode = longestPathRecurse(connected_node)
                recurseResult = max(recurseResult, longestPathForNode)

                if s[connected_node] == s[node]:
                    continue

                if longestPathForNode > longestPathA:
                    longestPathB = longestPathA
                    longestPathA = longestPathForNode
                elif longestPathForNode > longestPathB:
                    longestPathB = longestPathForNode

            recurseResult = max(recurseResult, longestPathA + longestPathB + 1)
            result = max(result, recurseResult)

            return longestPathA + 1

        longestPathRecurse(0)

        return result



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  92.71%
# Memory:   45.14%


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        nodes = defaultdict(list)

        for i, p in enumerate(parent):
            nodes[p].append(i)

        result = 0

        def longestPathRecurse(node):
            nonlocal result
            
            recurseResult = 1

            longestPathA = 0
            longestPathB = 0

            for connected_node in nodes[node]:
                longestPathForNode = longestPathRecurse(connected_node)
                recurseResult = recurseResult if recurseResult >= longestPathForNode else longestPathForNode

                if s[connected_node] == s[node]:
                    continue

                if longestPathForNode > longestPathA:
                    longestPathB = longestPathA
                    longestPathA = longestPathForNode
                elif longestPathForNode > longestPathB:
                    longestPathB = longestPathForNode

            recurseResult = max(recurseResult, longestPathA + longestPathB + 1)
            result = result if result >= recurseResult else recurseResult

            return longestPathA + 1

        longestPathRecurse(0)

        return result
