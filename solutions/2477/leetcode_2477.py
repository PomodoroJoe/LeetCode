#------------------------------------------------------
# Solution 1 - DFS w/ ugly gas correction for result
#------------------------------------------------------

# Runtime:  33.85%
# Memory:   09.81%


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        result = 0

        nodes = defaultdict(set)
        for road in roads:
            A = road[0]
            B = road[1]
            nodes[A].add(B)
            nodes[B].add(A)

        def dfs(node, parent):
            # process node
            people = 1
            gas = 0

            # process child nodes
            for next_node in nodes[node]:
                if next_node == parent:
                    continue

                new_people, used_gas = dfs(next_node, node)

                people += new_people
                gas += used_gas

            gas += ceil(people / seats)
            return people, gas

        people, gas = dfs(0, None)
        result = gas - ceil(people / seats)

        return result