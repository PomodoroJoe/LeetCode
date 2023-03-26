#------------------------------------------------------
# Solution 1 - find graphs, find result from graph len
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        result = 0

        connected_nodes = defaultdict(set)

        for a, b, in edges:
            connected_nodes[a].add(b)
            connected_nodes[b].add(a)

        # find all subgraphs
        graphs = []

        visited = [False] * n


        def graph_for_node(root):
            graph = set()

            queue = [root]
            while queue:
                node = queue.pop()

                if visited[node]:
                    continue

                visited[node] = True
                graph.add(node)

                for next_node in connected_nodes[node]:
                    queue.append(next_node)

            return graph


        for node in range(n):
            if visited[node]:
                continue

            graph = graph_for_node(node)
            graphs.append(graph)

        # find the result by multiplying the subgraph lengths
        for i in range(len(graphs)):
            current_graph = graphs[i]
            current_graph_len = len(current_graph)

            for j in range(i+1, len(graphs)):
                next_graph = graphs[j]
                next_graph_len = len(next_graph)

                result += current_graph_len * next_graph_len

        return result



#------------------------------------------------------
# Solution 2 - find graphs, optimized find result
#------------------------------------------------------

# Runtime:  29.17%
# Memory:   39.58%


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        result = 0

        connected_nodes = defaultdict(set)

        for a, b, in edges:
            connected_nodes[a].add(b)
            connected_nodes[b].add(a)

        # find all subgraphs
        graphs = []

        visited = [False] * n


        def graph_for_node(root):
            graph = set()

            queue = [root]
            while queue:
                node = queue.pop()

                if visited[node]:
                    continue

                visited[node] = True
                graph.add(node)

                for next_node in connected_nodes[node]:
                    queue.append(next_node)

            return graph


        for node in range(n):
            if visited[node]:
                continue

            graph = graph_for_node(node)
            graphs.append(graph)

        # find the result by multiplying the subgraph lengths
        graph_lengths = [len(graph) for graph in graphs]
        total = sum(graph_lengths)

        for graph_len in graph_lengths:
            total -= graph_len
            result += graph_len * total

        return result



#------------------------------------------------------
# Solution 3 - combined find graphs & find result
#------------------------------------------------------

# Runtime:  51.74%
# Memory:   39.58%


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        result = 0

        connected_nodes = defaultdict(set)

        for a, b, in edges:
            connected_nodes[a].add(b)
            connected_nodes[b].add(a)

        # find all subgraphs
        graphs = []

        visited = [False] * n


        def graph_for_node(root):
            graph = set()

            queue = [root]
            while queue:
                node = queue.pop()

                if visited[node]:
                    continue

                visited[node] = True
                graph.add(node)

                for next_node in connected_nodes[node]:
                    queue.append(next_node)

            return len(graph)


        total_graph_lengths = 0

        for node in range(n):
            if visited[node]:
                continue

            graph_len = graph_for_node(node)
            
            result += graph_len * total_graph_lengths
            total_graph_lengths += graph_len

        return result