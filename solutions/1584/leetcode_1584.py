#------------------------------------------------------
# Solution 1 - union find (ish)
#------------------------------------------------------

# Runtime:  55.70%
# Memory:   77.15%


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0

        point_count = len(points)

        def connectionCost(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        costs = []

        for i in range(point_count):
            for j in range(i + 1, point_count):
                p1 = points[i]
                p2 = points[j]

                cost = connectionCost(p1, p2)
                costs.append((cost, i, j))

        costs.sort()

        # index = point index, value = graph id
        graphs = [p for p in range(point_count)]
        graphs_set = set(graphs)

        while len(graphs_set) > 1 and costs:
            connection = costs.pop(0)

            cost, p1, p2 = connection

            if graphs[p1] == graphs[p2]:
                continue

            result += cost

            # union graphs
            g1 = graphs[p1]
            g2 = graphs[p2]

            if g2 < g1:
                g2, g1 = g1, g2

            for i in range(point_count):
                if graphs[i] == g2:
                    graphs[i] = g1

            if g2 in graphs_set:
                graphs_set.remove(g2)

        return result




#------------------------------------------------------
# Solution 2 - Solution 1 w/ deque
#------------------------------------------------------

# Runtime:  78.30%
# Memory:   71.14%


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0

        point_count = len(points)

        def connectionCost(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        costs = []

        for i in range(point_count):
            for j in range(i + 1, point_count):
                p1 = points[i]
                p2 = points[j]

                cost = connectionCost(p1, p2)
                costs.append((cost, i, j))

        costs.sort()
        costs = deque(costs)

        # index = point index, value = graph id
        graphs = [p for p in range(point_count)]
        graphs_set = set(graphs)

        while len(graphs_set) > 1 and costs:
            cost, p1, p2 = costs.popleft()

            if graphs[p1] == graphs[p2]:
                continue

            result += cost

            # union graphs
            g1 = graphs[p1]
            g2 = graphs[p2]

            if g2 < g1:
                g2, g1 = g1, g2

            for i in range(point_count):
                if graphs[i] == g2:
                    graphs[i] = g1

            if g2 in graphs_set:
                graphs_set.remove(g2)

        return result