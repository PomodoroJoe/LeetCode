#------------------------------------------------------
# Solution 1 - union
#------------------------------------------------------

# Runtime:   5.84%
# Memory:   84.55%


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graphs = []
        result_for_graph = defaultdict(int)

        for road in roads:
            a = road[0]
            b = road[1]

            found = False
            for i, graph in enumerate(graphs):
                if a in graph or b in graph:
                    graph.add(a)
                    graph.add(b)
                    result_for_graph[i] = min(result_for_graph[i], road[2])
                    found = True
                    break

            if not found:
                graphs.append(set([a, b]))
                result_for_graph[len(graphs) - 1] = road[2]

        # merge graphs
        result = inf
        start_graph = None
        for i, graph in enumerate(graphs):
            if 1 in graph:
                start_graph = graph
                result = result_for_graph[i]
                break

        done = False
        while not done:
            done = True
            next_graphs = []
            for i, graph in enumerate(graphs):
                if start_graph.intersection(graph):
                    start_graph = start_graph.union(graph)
                    done = False
                    result = min(result, result_for_graph[i])
                else:
                    next_graphs.append(graph)

            if not done:
                graphs = next_graphs

        # get result
        return result



#------------------------------------------------------
# Solution 2 - dfs
#------------------------------------------------------

# Runtime:  59.10%
# Memory:   80.48%



class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        cities = defaultdict(list)
        min_score = {}

        for road in roads:
            cities[road[0]].append(road[1])
            cities[road[1]].append(road[0])
            
            if road[0] not in min_score:
                min_score[road[0]] = road[2]
            else:
                min_score[road[0]] = min(road[2], min_score[road[0]])

            if road[1] not in min_score:
                min_score[road[1]] = road[2]
            else:
                min_score[road[1]] = min(road[2], min_score[road[1]])

        
        result = inf
        visited = set()

        paths = [1]

        while paths:
            city = paths.pop(-1)

            if city in visited:
                continue

            result = min(result, min_score[city])
            visited.add(city)

            paths += cities[city]

        return result