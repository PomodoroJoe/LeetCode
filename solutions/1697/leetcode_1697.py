#------------------------------------------------------
# Solution 1 - UnionFind (kinda)
#------------------------------------------------------

# Runtime:  29.648%
# Memory:   24.38%


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        class UnionFind():
            def __init__(self, n):
                self._parents = list(range(n))
                self._mapping = {}
                for i in range(n):
                    self._mapping[i] = [i]

            def find(self, n):
                while n != self._parents[n]:
                    n = self._parents[n]
                return n

            def union(self, a, b):
                parent_a = self.find(a)
                parent_b = self.find(b)

                if parent_a == parent_b:
                    return

                if parent_a < parent_b:
                    for node in self._mapping[parent_b]:
                        self._parents[node] = parent_a
                    self._mapping[parent_a] += self._mapping[parent_b]
                    self._mapping[parent_b] = []
                else:
                    for node in self._mapping[parent_a]:
                        self._parents[node] = parent_b
                    self._mapping[parent_b] += self._mapping[parent_a]
                    self._mapping[parent_a] = []

        
        sorted_edges = sorted(edgeList, key = lambda x: x[2])

        query_index_map = {}
        for i, q in enumerate(queries):
            query_index_map[tuple(q)] = i

        sorted_queries = sorted(queries, key = lambda x: x[2])

        sub_graphs = UnionFind(n)

        current_edge = 0
        result = [True] * len(queries)

        for query in sorted_queries:
            q1, q2, limit = query

            while current_edge < len(sorted_edges) and sorted_edges[current_edge][2] < limit:
                n1, n2, d = sorted_edges[current_edge]
                sub_graphs.union(n1, n2)
                current_edge += 1

            query_index = query_index_map[tuple(query)]
            result[query_index] = sub_graphs.find(q1) == sub_graphs.find(q2)

        return result