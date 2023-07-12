#------------------------------------------------------
# Solution 1 - recursive w/ visited set
#------------------------------------------------------

# Runtime:  23.23%
# Memory:   65.94%


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []

        visited = None

        dp = {}

        def isSafeNode(node):
            if node in dp:
                return dp[node]

            if node in visited:
                dp[node] = False
                return False
            
            visited.add(node)

            connected_nodes = graph[node]

            for connected_node in connected_nodes:
                if not isSafeNode(connected_node):
                    dp[node] = False
                    return False

            dp[node] = True
            return True


        for node in range(len(graph)):
            visited = set()
            if isSafeNode(node):
                result.append(node)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ dp disctionary
#------------------------------------------------------

# Runtime:  52.41%
# Memory:   75.79%


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []

        dp = {}

        def isSafeNode(node):
            if node in dp:
                return dp[node]

            dp[node] = False

            connected_nodes = graph[node]

            for connected_node in connected_nodes:
                if not isSafeNode(connected_node):
                    dp[node] = False
                    return False

            dp[node] = True
            return True


        for node in range(len(graph)):
            if isSafeNode(node):
                result.append(node)

        return result



#------------------------------------------------------
# Solution 3 - Solution 2 w/ dp list
#------------------------------------------------------

# Runtime:  99.32%
# Memory:   91.50%


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []

        dp = [None] * len(graph)

        def isSafeNode(node):
            if dp[node] != None:
                return dp[node]

            dp[node] = False

            connected_nodes = graph[node]

            for connected_node in connected_nodes:
                if not isSafeNode(connected_node):
                    dp[node] = False
                    return False

            dp[node] = True
            return True


        for node in range(len(graph)):
            if isSafeNode(node):
                result.append(node)

        return result