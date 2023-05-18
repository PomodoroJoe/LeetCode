#------------------------------------------------------
# Solution 1 - sets
#------------------------------------------------------

# Runtime:  39.98%
# Memory:   23.10%


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        all_nodes = set()
        destination_nodes = set()

        for f, t in edges:
            all_nodes.add(f)
            destination_nodes.add(t)

        return all_nodes - destination_nodes



#------------------------------------------------------
# Solution 2 - lists
#------------------------------------------------------

# Runtime:  81.20%
# Memory:   16.24%


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        nodes = [1] * n

        for s, d in edges:
            nodes[d] = 0

        result = []
        for node, val in enumerate(nodes):
            if val:
                result.append(node)

        return result