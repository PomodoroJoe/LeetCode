
#------------------------------------------------------
# Solution 1 - dfs
#------------------------------------------------------

# Runtime:  16.24%
# Memory:   38.34%


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if n < 2:
            return 0

        if len(connections) < n - 1:
            return -1

        # graph  (key = computer, value = all connected computers)

        graph = defaultdict(set)

        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        def network_for_computer(root):
            network = set()

            queue = [root]
            visited = set()

            while queue:
                computer = queue.pop(0)

                if computer in visited:
                    continue

                visited.add(computer)
                network.add(computer)

                for connected_computer in graph[computer]:
                    queue.append(connected_computer)

            return network

        need_to_find_network = [True for _ in range(n)]
        network_count = 0

        for computer in range(n):
            if need_to_find_network[computer]:
                network = network_for_computer(computer)
                network_count += 1

                for connected_computer in network:
                    need_to_find_network[connected_computer] = False

        return network_count - 1




#------------------------------------------------------
# Solution 2 - dfs
#------------------------------------------------------

# Runtime:  31.26%
# Memory:   38.43%


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if n < 2:
            return 0

        if len(connections) < n - 1:
            return -1

        # graph  (key = computer, value = all connected computers)

        graph = defaultdict(set)

        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        def network_for_computer(root):
            network = set()

            queue = [root]
            visited = set()

            while queue:
                computer = queue.pop(0)

                if computer in visited:
                    continue

                visited.add(computer)
                network.add(computer)

                for connected_computer in graph[computer]:
                    if connected_computer not in visited:
                        queue.append(connected_computer)

            return network

        need_to_find_network = [True for _ in range(n)]
        network_count = 0

        for computer in range(n):
            if need_to_find_network[computer]:
                network = network_for_computer(computer)
                network_count += 1

                for connected_computer in network:
                    need_to_find_network[connected_computer] = False

        return network_count - 1



#------------------------------------------------------
# Solution 5 - dfs
#------------------------------------------------------

# Runtime:  49.48%
# Memory:   38.43%


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if n < 2:
            return 0

        if len(connections) < n - 1:
            return -1

        # graph  (key = computer, value = all connected computers)

        graph = defaultdict(set)

        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        def network_for_computer(root):
            network = set([root])

            queue = [root]
            visited = set()

            while queue:
                computer = queue.pop(-1)

                if computer in visited:
                    continue

                visited.add(computer)
                network.add(computer)

                for connected_computer in graph[computer]:
                    if connected_computer not in visited:
                        queue.append(connected_computer)

            return network

        need_to_find_network = [True for _ in range(n)]
        network_count = 0

        for computer in range(n):
            if need_to_find_network[computer]:
                network = network_for_computer(computer)
                network_count += 1

                for connected_computer in network:
                    need_to_find_network[connected_computer] = False

        return network_count - 1