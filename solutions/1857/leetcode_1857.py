#------------------------------------------------------
# Solution 1 - Kahn's Algorithm
#------------------------------------------------------

# Runtime:  95.15%
# Memory:   78.79%


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        result = -1

        node_count = len(colors)

        # "key" = node, value = per color count
        color_counts_for_node = [[0] * 26 for _ in range(node_count)]

        def index_for_color(color):
            return ord(color) - ord('a')

        # key = node, value = list of connected nodes
        edge_map = defaultdict(list)
        
        # "key" = node, value = count of input edges
        input_edge_count = [0] * node_count

        for source, dest in edges:
            edge_map[source].append(dest)
            input_edge_count[dest] += 1
        
        start_nodes = []
        for node, count in enumerate(input_edge_count):
            if count == 0:
                start_nodes.append(node)

        queue = start_nodes
        processed_node_count = 0

        while queue:
            node = queue.pop(0)
            processed_node_count += 1

            # process this node
            color = colors[node]
            color_counts_for_node[node][index_for_color(color)] += 1

            result = max(result, color_counts_for_node[node][index_for_color(color)])

            current_colors = color_counts_for_node[node]

            for connected_node in edge_map[node]:
                # push data
                connected_node_colors = color_counts_for_node[connected_node]
                for i in range(26):
                    if current_colors[i] > connected_node_colors[i]:
                        connected_node_colors[i] = current_colors[i]

                input_edge_count[connected_node] -= 1
                if input_edge_count[connected_node] == 0:
                    queue.append(connected_node)


        if processed_node_count != node_count:
            return -1

        return result