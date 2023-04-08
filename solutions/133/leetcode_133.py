#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  89.60%
# Memory:   65.11%


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # key = node_id (val) --> value = cloned_node
        cloned_nodes = {}

        def cloneNode(n):
            if n == None:
                return None

            new_node = Node()
            new_node.val = n.val

            cloned_nodes[n.val] = new_node

            for neighbor in n.neighbors:
                node_id = neighbor.val

                new_neighbor = None
                if node_id in cloned_nodes:
                    new_neighbor = cloned_nodes[node_id]
                else:
                    new_neighbor = cloneNode(neighbor)
                    cloned_nodes[node_id] = new_neighbor

                new_node.neighbors.append(new_neighbor)

            return new_node

        return cloneNode(node)




#------------------------------------------------------
# Solution 2 - cleaner recursive
#------------------------------------------------------

# Runtime:  89.60%
# Memory:   17.25%


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # key = node_id (val) --> value = cloned_node
        cloned_nodes = {}

        def cloneNode(n):
            if n == None:
                return None

            new_node = Node()
            new_node.val = n.val

            cloned_nodes[n.val] = new_node

            for neighbor in n.neighbors:
                node_id = neighbor.val
                new_neighbor = cloned_nodes[node_id] if node_id in cloned_nodes else cloneNode(neighbor)
                new_node.neighbors.append(new_neighbor)

            return new_node

        return cloneNode(node)