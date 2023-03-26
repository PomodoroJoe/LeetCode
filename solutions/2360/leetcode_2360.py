#------------------------------------------------------
# Solution 1 - find cycles then find cycle length
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result = -1

        n = len(edges)


        def cycle_for_node(start_node):
            node = start_node

            seen_nodes = set()

            while node != -1 and node not in seen_nodes:
                seen_nodes.add(node)

                next_node = edges[node]
                node = next_node

            return node


        def cycle_length_for_node(start_node):
            node = start_node

            seen_nodes = set()
            count = 0

            while node not in seen_nodes:
                seen_nodes.add(node)
                count += 1

                next_node = edges[node]
                node = next_node

            return count


        for start_node in range(n):
            cycle_start = cycle_for_node(start_node)

            if cycle_start != -1:
                cycle_length = cycle_length_for_node(cycle_start)
                result = max(result, cycle_length)

        return result



#------------------------------------------------------
# Solution 2 - find cycle lengths directly
#------------------------------------------------------

# Runtime:  65.48%
# Memory:   82.90%


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result = -1

        n = len(edges)

        seen_nodes = {}
        count = 0

        def cycle_length_for_node(start_node):
            nonlocal count

            node = start_node
            start_count = count

            while node != -1 and node not in seen_nodes:
                seen_nodes[node] = count
                count += 1

                next_node = edges[node]
                node = next_node

            if node == -1:
                return -1

            if seen_nodes[node] < start_count:
                return -1

            return count - seen_nodes[node]


        for start_node in range(n):
            cycle_length = cycle_length_for_node(start_node)

            if cycle_length != -1:
                result = max(result, cycle_length)

        return result


#------------------------------------------------------
# Solution 3 - optimized find cycle lengths
#------------------------------------------------------

# Runtime:  90.97%
# Memory:   98.39%


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result = -1

        n = len(edges)

        seen_nodes = [0] * n
        count = 1

        def cycle_length_for_node(start_node):
            nonlocal count

            node = start_node
            start_count = count

            while node != -1 and seen_nodes[node] == 0:
                seen_nodes[node] = count
                count += 1

                node = edges[node]

            if node == -1:
                return -1

            if seen_nodes[node] < start_count:
                return -1

            return count - seen_nodes[node]


        for start_node in range(n):
            cycle_length = cycle_length_for_node(start_node)
            result = result if result > cycle_length else cycle_length

        return result
