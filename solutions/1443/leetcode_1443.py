#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  67.52%
# Memory:   10.19%


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodes = defaultdict(set)

        for edge in edges:
            nodes[edge[0]].add(edge[1])
            nodes[edge[1]].add(edge[0])

        def minTimeRecurse(node, parent):
            result = 0

            # leaf
            if len(nodes[node]) == 1 and node != 0:
                return 2 if hasApple[node] else 0

            for connected_node in nodes[node]:
                if connected_node == parent:
                    continue
                result += minTimeRecurse(connected_node, node)

            if (result != 0 or hasApple[node]) and node != 0:
                result += 2

            return result

        return minTimeRecurse(0, 0)



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  82.80%
# Memory:   74.52%

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodes = defaultdict(list)

        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)

        def minTimeRecurse(node, parent):
            result = 0

            # leaf
            if len(nodes[node]) == 1 and node != 0:
                return 2 if hasApple[node] else 0

            for connected_node in nodes[node]:
                if connected_node == parent:
                    continue
                result += minTimeRecurse(connected_node, node)

            if (result != 0 or hasApple[node]) and node != 0:
                result += 2

            return result

        return minTimeRecurse(0, 0)
