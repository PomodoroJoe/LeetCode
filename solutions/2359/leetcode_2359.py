#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  90.80%
# Memory:   40.81%


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        result = -1

        dist_map1 = {node1: 0}   # node: dist to node 1
        dist_map2 = {node2: 0}   # node: dist to node 2

        n1 = node1
        d1 = 0

        while d1 < len(dist_map1):
            n1 = edges[n1]
            d1 += 1

            if n1 == -1:
                break

            if n1 not in dist_map1:
                dist_map1[n1] = d1

        n2 = node2
        d2 = 0

        while d2 < len(dist_map2):
            n2 = edges[n2]
            d2 += 1

            if n2 == -1:
                break

            if n2 not in dist_map2:
                dist_map2[n2] = d2


        graph1 = set(dist_map1.keys())
        graph2 = set(dist_map2.keys())

        shared_nodes = graph1.intersection(graph2)
        
        min_max_dist = inf
        for node in shared_nodes:
            d1 = dist_map1[node]
            d2 = dist_map2[node]

            max_dist = max(d1, d2)

            if max_dist == min_max_dist:
                result = min(result, node)

            if max_dist < min_max_dist:
                min_max_dist = max_dist
                result = node

        return result



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  85.63%
# Memory:   45.40%


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        result = -1

        dist_map1 = {node1: 0}   # node: dist to node 1
        dist_map2 = {node2: 0}   # node: dist to node 2

        n = node1
        d = 0

        while d < len(dist_map1):
            n = edges[n]
            d += 1

            if n == -1:
                break

            if n not in dist_map1:
                dist_map1[n] = d

        n = node2
        d = 0

        while d < len(dist_map2):
            n = edges[n]
            d += 1

            if n == -1:
                break

            if n not in dist_map2:
                dist_map2[n] = d


        graph1 = set(dist_map1.keys())
        graph2 = set(dist_map2.keys())

        shared_nodes = graph1.intersection(graph2)
        
        min_max_dist = inf
        for node in shared_nodes:
            max_dist = max(dist_map1[node], dist_map2[node])

            if max_dist == min_max_dist:
                result = min(result, node)

            if max_dist < min_max_dist:
                min_max_dist = max_dist
                result = node

        return result