#------------------------------------------------------
# Solution 1 - follow the graph
#------------------------------------------------------

# Runtime:  43.58%
# Memory:   31.77%


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set_A = set()
        set_B = set()

        n = len(graph)

        for i in range(n):
            if i in set_A or i in set_B:
                continue

            stack = [i]

            while stack:
                node = stack.pop(0)

                current_set = set_A
                opposite_set = set_B
                
                if node in set_B:
                    current_set = set_B
                    opposite_set = set_A

                for connected_node in graph[node]:
                    if connected_node in current_set:
                        return False

                    if connected_node not in opposite_set:
                        opposite_set.add(connected_node)
                        stack.append(connected_node)
            
        return True



#------------------------------------------------------
# Solution 2 - follow the graph w/ deque
#------------------------------------------------------

# Runtime:  69.79%
# Memory:   21.33%


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set_A = set()
        set_B = set()

        n = len(graph)

        for i in range(n):
            if i in set_A or i in set_B:
                continue

            stack = deque([i])

            while stack:
                node = stack.popleft()

                current_set = set_A
                opposite_set = set_B
                
                if node in set_B:
                    current_set = set_B
                    opposite_set = set_A

                for connected_node in graph[node]:
                    if connected_node in current_set:
                        return False

                    if connected_node not in opposite_set:
                        opposite_set.add(connected_node)
                        stack.append(connected_node)
            
        return True