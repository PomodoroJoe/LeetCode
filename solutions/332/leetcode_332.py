#------------------------------------------------------
# Solution 1 - DFS (with backtracking?)
#------------------------------------------------------

# Runtime:  45.39%
# Memory:   99.00%


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        # key = departure city, value = list of destination cities
        connection_map = defaultdict(list)
        for src, dst in tickets:
            connection_map[src].append(dst)

        for src in connection_map:
            connection_map[src].sort()

        stack = ["JFK"]

        while stack:
            current_city = stack[-1]

            if current_city in connection_map and connection_map[current_city]:
                dst = connection_map[current_city].pop(0)
                stack.append(dst)
            else:
                stack.pop(-1)
                result.append(current_city)

        return result[::-1]



#------------------------------------------------------
# Solution 2 - Solution 1 w/ deque
#------------------------------------------------------

# Runtime:  97.29%
# Memory:   95.49%


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        # key = departure city, value = list of destination cities
        connection_map = defaultdict(list)
        for src, dst in tickets:
            connection_map[src].append(dst)

        for src in connection_map:
            connection_map[src].sort()

        stack = deque(["JFK"])

        while stack:
            current_city = stack[-1]

            if current_city in connection_map and connection_map[current_city]:
                dst = connection_map[current_city].pop(0)
                stack.append(dst)
            else:
                stack.pop()
                result.append(current_city)

        return result[::-1]