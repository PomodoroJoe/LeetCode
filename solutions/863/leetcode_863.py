#------------------------------------------------------
# Solution 1 - tree to graph w/ BFS
#------------------------------------------------------

# Runtime:  46.77%
# Memory:   59.00%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []

        # key = node value, value = list of connected nodes
        node_to_edge_map = defaultdict(list)

        def buildGraph(rootNode):
            if not rootNode:
                return 

            if rootNode.left:
                node_to_edge_map[rootNode.val].append(rootNode.left.val)
                node_to_edge_map[rootNode.left.val].append(rootNode.val)
                buildGraph(rootNode.left)

            if rootNode.right:
                node_to_edge_map[rootNode.val].append(rootNode.right.val)
                node_to_edge_map[rootNode.right.val].append(rootNode.val)
                buildGraph(rootNode.right)

        buildGraph(root)

        queue = [(target.val, 0)]
        visited = set()

        while queue:
            node, dist = queue.pop(0)

            if node in visited:
                continue

            visited.add(node)

            if dist == k:
                result.append(node)
                continue

            for connected_node in node_to_edge_map[node]:
                if connected_node not in visited:
                    queue.append((connected_node, dist + 1))

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ deque
#------------------------------------------------------

# Runtime:  65.35%
# Memory:   35.18%


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []

        # key = node value, value = list of connected nodes
        node_to_edge_map = defaultdict(list)

        def buildGraph(rootNode):
            if not rootNode:
                return 

            if rootNode.left:
                node_to_edge_map[rootNode.val].append(rootNode.left.val)
                node_to_edge_map[rootNode.left.val].append(rootNode.val)
                buildGraph(rootNode.left)

            if rootNode.right:
                node_to_edge_map[rootNode.val].append(rootNode.right.val)
                node_to_edge_map[rootNode.right.val].append(rootNode.val)
                buildGraph(rootNode.right)

        buildGraph(root)

        queue = deque([(target.val, 0)])
        visited = set()

        while queue:
            node, dist = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            if dist == k:
                result.append(node)
                continue

            for connected_node in node_to_edge_map[node]:
                if connected_node not in visited:
                    queue.append((connected_node, dist + 1))

        return result


#------------------------------------------------------
# Solution 3 - Solution 2 w/o continue
#------------------------------------------------------

# Runtime:  82.60%
# Memory:   59.00%


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []

        # key = node value, value = list of connected nodes
        node_to_edge_map = defaultdict(list)

        def buildGraph(rootNode):
            if not rootNode:
                return 

            if rootNode.left:
                node_to_edge_map[rootNode.val].append(rootNode.left.val)
                node_to_edge_map[rootNode.left.val].append(rootNode.val)
                buildGraph(rootNode.left)

            if rootNode.right:
                node_to_edge_map[rootNode.val].append(rootNode.right.val)
                node_to_edge_map[rootNode.right.val].append(rootNode.val)
                buildGraph(rootNode.right)

        buildGraph(root)

        queue = deque([(target.val, 0)])
        visited = set()

        while queue:
            node, dist = queue.popleft()

            if node not in visited:
                visited.add(node)

                if dist == k:
                    result.append(node)
                    continue

                for connected_node in node_to_edge_map[node]:
                    if connected_node not in visited:
                        queue.append((connected_node, dist + 1))

        return result