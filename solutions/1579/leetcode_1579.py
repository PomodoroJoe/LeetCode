#------------------------------------------------------
# Solution 2 - UnionFind
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind():

            def __init__(self, n):
                self.node_groups = list(range(n + 1))

            def find(self, n):
                while self.node_groups[n] != n:
                    n = self.node_groups[n]
                return n

            def union(self, n1, n2):
                group_1 = self.find(n1)
                group_2 = self.find(n2)

                if group_1 == group_2:
                    return

                main_group = min(group_1, group_2)
                merging_group = group_1 if group_1 != main_group else group_2

                self.node_groups[merging_group] = main_group


        sorted_edges = sorted(edges, key = lambda x: -x[0])

        alice_nodes = UnionFind(n)
        bob_nodes = UnionFind(n)

        alice_edge_count = 0
        bob_edge_count = 0

        removed_count = 0


        for t, a, b in sorted_edges:

            if t == 3:
                if alice_nodes.find(a) != alice_nodes.find(b):
                    alice_nodes.union(a, b)
                    bob_nodes.union(a, b)

                    alice_edge_count += 1
                    bob_edge_count += 1
                else:
                    removed_count += 1


            elif t == 2:
                if bob_nodes.find(a) != bob_nodes.find(b):
                    bob_nodes.union(a, b)
                    bob_edge_count += 1
                else:
                    removed_count += 1


            else:
                if alice_nodes.find(a) != alice_nodes.find(b):
                    alice_nodes.union(a, b)
                    alice_edge_count += 1
                else:
                    removed_count += 1


        return removed_count if (alice_edge_count == n-1 and bob_edge_count == n-1) else -1



#------------------------------------------------------
# Solution 3 - UnionFind w/ optimized find
#------------------------------------------------------

# Runtime:  72.50%
# Memory:   20.63%


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind():

            def __init__(self, n):
                self.node_groups = list(range(n + 1))

            def find(self, n):
                while self.node_groups[n] != n:
                    self.node_groups[n] = self.node_groups[self.node_groups[n]]
                    n = self.node_groups[n]
                return n

            def union(self, n1, n2):
                group_1 = self.find(n1)
                group_2 = self.find(n2)

                if group_1 == group_2:
                    return

                main_group = group_1 if group_1 < group_2 else group_2
                merging_group = group_1 if group_1 != main_group else group_2

                self.node_groups[merging_group] = main_group


        sorted_edges = sorted(edges, key = lambda x: -x[0])

        alice_nodes = UnionFind(n)
        bob_nodes = UnionFind(n)

        alice_edge_count = 0
        bob_edge_count = 0

        removed_count = 0


        for t, a, b in sorted_edges:

            if t == 3:
                if alice_nodes.find(a) != alice_nodes.find(b):
                    alice_nodes.union(a, b)
                    bob_nodes.union(a, b)

                    alice_edge_count += 1
                    bob_edge_count += 1
                else:
                    removed_count += 1


            elif t == 2:
                if bob_nodes.find(a) != bob_nodes.find(b):
                    bob_nodes.union(a, b)
                    bob_edge_count += 1
                else:
                    removed_count += 1


            else:
                if alice_nodes.find(a) != alice_nodes.find(b):
                    alice_nodes.union(a, b)
                    alice_edge_count += 1
                else:
                    removed_count += 1


        return removed_count if (alice_edge_count == n-1 and bob_edge_count == n-1) else -1