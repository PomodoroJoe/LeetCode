#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  25.37%
# Memory:   25.74%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0

        LEFT = -1 
        RIGHT = 1

        def longestZigZagRecurse(node, direction, count):
            nonlocal result

            if not node:
                return

            result = max(result, count)

            if direction == LEFT:
                # continue zigzag
                longestZigZagRecurse(node.right, RIGHT, count + 1)
                # start a new zigzag
                longestZigZagRecurse(node.left, LEFT, 1)

            if direction == RIGHT:
                # continue zigzag
                longestZigZagRecurse(node.left, LEFT, count + 1)
                # start a new zigzag
                longestZigZagRecurse(node.right, RIGHT, 1)

        longestZigZagRecurse(root, LEFT, 0)
        longestZigZagRecurse(root, RIGHT, 0)

        return result



#------------------------------------------------------
# Solution 4 - Solution 1 optimized
#------------------------------------------------------

# Runtime:  43.20%
# Memory:   25.74%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0

        LEFT = -1 
        RIGHT = 1

        def longestZigZagRecurse(node, direction, count):
            nonlocal result

            if not node:
                return

            result = result if result > count else count

            if direction == LEFT:
                longestZigZagRecurse(node.right, RIGHT, count + 1)
                longestZigZagRecurse(node.left, LEFT, 1)
            else:
                longestZigZagRecurse(node.left, LEFT, count + 1)
                longestZigZagRecurse(node.right, RIGHT, 1)

        longestZigZagRecurse(root, LEFT, 0)
        longestZigZagRecurse(root, RIGHT, 0)

        return result



#------------------------------------------------------
# Solution 5 - iterative
#------------------------------------------------------

# Runtime:   9.20%
# Memory:  100.00%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0

        LEFT = -1 
        RIGHT = 1

        queue = [(root, RIGHT, 0), (root, LEFT, 0)]

        while queue:
            node, direction, count = queue.pop(0)

            if not node:
                continue

            result = max(result, count)

            if direction == LEFT:
                queue.append((node.right, RIGHT, count + 1))
                queue.append((node.left, LEFT, 1))

            if direction == RIGHT:
                queue.append((node.left, LEFT, count + 1))
                queue.append((node.right, RIGHT, 1))

        return result



#------------------------------------------------------
# Solution 8 - Solution 5 optimized w/ deque
#------------------------------------------------------

# Runtime:  91.18%
# Memory:   99.25%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0

        LEFT = -1 
        RIGHT = 1

        queue = deque([(root, 0, 0)])

        while queue:
            node, direction, count = queue.popleft()

            if not node:
                continue

            result = result if result > count else count

            if direction == LEFT:
                queue.append((node.right, RIGHT, count + 1))
                queue.append((node.left, LEFT, 1))
                continue

            if direction == RIGHT:
                queue.append((node.left, LEFT, count + 1))
                queue.append((node.right, RIGHT, 1))
                continue

            queue.append((node.right, RIGHT, count + 1))
            queue.append((node.left, LEFT, count + 1))

        return result