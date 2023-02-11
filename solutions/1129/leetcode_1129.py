#------------------------------------------------------
# Solution 1 - graph traversal (BFS)
#------------------------------------------------------

# Runtime:  57.92%
# Memory:   73.17%


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        result = [-1] * n

        red_links = defaultdict(set)
        blue_links = defaultdict(set)

        for edge in redEdges:
            red_links[edge[0]].add(edge[1])

        for edge in blueEdges:
            blue_links[edge[0]].add(edge[1])

        RED = 0
        BLUE = 1

        # node, next_color, path_len

        queue = [(0, RED, 0), (0, BLUE, 0)]
        visited = set()

        while queue:
            node, next_color, length = queue.pop(0)

            if result[node] == -1 or result[node] > length:
                result[node] = length

            visited.add((node, next_color))

            if next_color == RED:
                for next_node in red_links[node]:
                    if (next_node, BLUE) in visited:
                        continue
                    queue.append((next_node, BLUE, length + 1))

            if next_color == BLUE:
                for next_node in blue_links[node]:
                    if (next_node, RED) in visited:
                        continue
                    queue.append((next_node, RED, length + 1))

        return result