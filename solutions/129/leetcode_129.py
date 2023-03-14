#------------------------------------------------------
# Solution 1 - recursive depth first search (DFS)
#------------------------------------------------------

# Runtime:  42.80%
# Memory:   95.89%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def DFS(node, val):
            if not node:
                return 0

            cur_value = (10 * val) + node.val

            if node.left == None and node.right == None:
                return cur_value

            return DFS(node.left, cur_value) + DFS(node.right, cur_value)

        result = DFS(root, 0)
        return result 




#------------------------------------------------------
# Solution 2 - iterative depth first search (DFS)
#------------------------------------------------------

# Runtime:  88.93%
# Memory:   95.89%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        queue = [(root, 0)]

        while queue:
            node, val = queue.pop(0)

            cur_value = (10 * val) + node.val

            if node.left == None and node.right == None:
                result += cur_value
                continue

            if node.left != None:
                queue.append((node.left, cur_value))

            if node.right != None:
                queue.append((node.right, cur_value))

        return result




#------------------------------------------------------
# Solution 3 - iterative depth first search (DFS)
#------------------------------------------------------

# Runtime:  92.24%
# Memory:   54.57%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        queue = [(root, 0)]

        while queue:
            node, val = queue.pop(0)

            if node == None:
                continue

            cur_value = (10 * val) + node.val

            if node.left == None and node.right == None:
                result += cur_value
                continue

            queue += [((node.left, cur_value)), ((node.right, cur_value))]

        return result
