#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  87.10%
# Memory:   15.22%


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        result = 0

        graph = defaultdict(set)

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)


        def networkRangeForCities(a, b):
            rank = len(graph[a]) + len(graph[b])
            if a in graph[b]:
                rank -= 1
            return rank


        for a in range(n):
            for b in range(a + 1, n):
                rank = networkRangeForCities(a, b)
                result = max(result, rank)

        return result


#------------------------------------------------------
# Solution 2 - Solution 1 w/o helper function
#------------------------------------------------------

# Runtime:  73.91%
# Memory:   64.35%


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        result = 0

        graph = defaultdict(set)

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        for a in range(n):
            for b in range(a + 1, n):
                rank = len(graph[a]) + len(graph[b])
                if a in graph[b]:
                    rank -= 1

                result = max(result, rank)

        return result


#------------------------------------------------------
# Solution 3 - Solution 1 w/ custom max
#------------------------------------------------------

# Runtime:  94.78%
# Memory:   15.22%


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        result = 0

        graph = defaultdict(set)

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)


        def networkRangeForCities(a, b):
            rank = len(graph[a]) + len(graph[b])
            if a in graph[b]:
                rank -= 1
            return rank


        for a in range(n):
            for b in range(a + 1, n):
                rank = networkRangeForCities(a, b)
                result = result if result > rank else rank

        return result