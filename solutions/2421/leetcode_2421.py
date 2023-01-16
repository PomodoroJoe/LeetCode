#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  80.21%
# Memory:   52.34%


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        result = len(vals)

        nodes = defaultdict(set)
        for a, b in edges:
            nodes[a].add(b)
            nodes[b].add(a)

        nodes_by_value = defaultdict(set)
        for i in range(len(vals)):
            nodes_by_value[vals[i]].add(i)

        groups = {}

        def group_nodes(n0, n1):
            groups[find_group(n0)] = find_group(n1)

        def find_group(n):
            if n not in groups:
                groups[n] = n

            if groups[n] != n:
                groups[n] = find_group(groups[n])

            return groups[n]

        values = sorted(nodes_by_value.keys())
        for val in values:
            for node in nodes_by_value[val]:
                for connected_node in nodes[node]:
                    if vals[connected_node] > val:
                        continue

                    group_nodes(node, connected_node)

            # count nodes of val in groups
            groups_by_value = defaultdict(int)
            for node in nodes_by_value[val]:
                node_group = find_group(node)
                groups_by_value[node_group] += 1

            for group in groups_by_value:
                result += math.comb(groups_by_value[group], 2)

        return result
