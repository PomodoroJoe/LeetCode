#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  98.72%
# Memory:   70.51%


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        nodes = defaultdict(set)

        for a, b in edges:
            nodes[a].add(b)
            nodes[b].add(a)

        result = [0 for _ in range(n)]

        label_count = defaultdict(int)

        def countSubTreesRecurse(node, parent):
            label = labels[node]

            parent_count = label_count[label]

            label_count[label] += 1

            for connected_node in nodes[node]:
                if connected_node == parent:
                    continue

                countSubTreesRecurse(connected_node, node)

            result[node] = label_count[label] - parent_count

        countSubTreesRecurse(0, -1)

        return result


#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  98.72%
# Memory:   93.19%


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        nodes = defaultdict(list)

        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)

        result = [0 for _ in range(n)]

        label_count = defaultdict(int)

        def countSubTreesRecurse(node, parent):
            label = labels[node]

            parent_count = label_count[label]

            label_count[label] += 1

            for connected_node in nodes[node]:
                if connected_node == parent:
                    continue

                countSubTreesRecurse(connected_node, node)

            result[node] = label_count[label] - parent_count

        countSubTreesRecurse(0, -1)

        return result
