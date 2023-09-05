#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  46.78%
# Memory:   37.47%


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        new_head = None
        prev_node = None

        # key = input list node, value = output list node
        old_node_to_new_node_map = {}

        def DeepCopy(node):
            if node not in old_node_to_new_node_map:
                new_node = Node(node.val)
                old_node_to_new_node_map[node] = new_node
            
            new_node = old_node_to_new_node_map[node]

            if node.random == None:
                return new_node

            if node.random not in old_node_to_new_node_map:
                new_random_node = Node(node.random.val)
                old_node_to_new_node_map[node.random] = new_random_node

            new_random_node = old_node_to_new_node_map[node.random]
            new_node.random = new_random_node

            return new_node

        while node:
            # process node
            new_node = DeepCopy(node)

            if not new_head:
                new_head = new_node

            if prev_node:
                prev_node.next = new_node
            else:
                new_head = new_node

            prev_node = new_node
            node = node.next


        return new_head