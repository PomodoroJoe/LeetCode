#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  86.26%
# Memory:   46.40%


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.connections = [[] for _ in range(n)]

        for n1, n2, cost in edges:
            self.connections[n1].append((n2, cost))
        

    def addEdge(self, edge: List[int]) -> None:
        n1, n2, cost = edge
        self.connections[n1].append((n2, cost))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = [(0, node1)]
        cache = [inf] * len(self.connections)
        cache[node1] = 0

        while queue:
            cost, node = heapq.heappop(queue)

            if node == node2:
                return cost

            if cost > cache[node]:
                continue

            for next_node, additional_cost in self.connections[node]:
                total_cost = cost + additional_cost
                if total_cost < cache[next_node]:
                    cache[next_node] = total_cost
                    heapq.heappush(queue, (total_cost, next_node))

        return cache[node2] if cache[node2] != inf else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)