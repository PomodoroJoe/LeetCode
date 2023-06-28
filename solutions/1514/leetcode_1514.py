#------------------------------------------------------
# Solution 1 - queue
#------------------------------------------------------

# Runtime:   6.70%
# Memory:   71.41%


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        result = 0

        node_map = defaultdict(list)

        for i in range(len(edges)):
            edge = edges[i]
            prob = succProb[i]

            a = edge[0]
            b = edge[1]

            node_map[a].append((b, prob))
            node_map[b].append((a, prob))

        queue = [(start, 1)]
        visited_probs = [0] * n

        while queue:
            node, prob = queue.pop(0)

            if node == end:
                continue

            connected_nodes = node_map[node]

            for connected_node, connection_prob in connected_nodes:
                new_prob = prob * connection_prob

                if visited_probs[connected_node] < new_prob:
                    visited_probs[connected_node] = new_prob
                    queue.append((connected_node, new_prob))

        result = visited_probs[end]
        return result



#------------------------------------------------------
# Solution 2 - max heap
#------------------------------------------------------

# Runtime:  86.31%
# Memory:   16.00%


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        result = 0

        node_map = defaultdict(list)

        for i in range(len(edges)):
            edge = edges[i]
            prob = succProb[i]

            a = edge[0]
            b = edge[1]

            node_map[a].append((b, prob))
            node_map[b].append((a, prob))

        heap = [(-1, start)]
        visited_probs = [0] * n

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob

            if node == end:
                break

            connected_nodes = node_map[node]

            for connected_node, connection_prob in connected_nodes:
                new_prob = prob * connection_prob

                if visited_probs[connected_node] < new_prob:
                    visited_probs[connected_node] = new_prob

                    heapq.heappush(heap, (-new_prob, connected_node))

        result = visited_probs[end]
        return result