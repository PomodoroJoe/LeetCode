#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  35.10%
# Memory:   21.24%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
       
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        left_option = inf
        if root.left:
            left_option = self.minDepth(root.left)

        right_option = inf
        if root.right:
            right_option = self.minDepth(root.right)

        return 1 + min(left_option, right_option)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ custom min
#------------------------------------------------------

# Runtime:  30.93%
# Memory:   63.15%


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        left_option = inf
        if root.left:
            left_option = self.minDepth(root.left)

        right_option = inf
        if root.right:
            right_option = self.minDepth(root.right)

        return 1 + (left_option if left_option < right_option else right_option)



#------------------------------------------------------
# Solution 3 - iterative
#------------------------------------------------------

# Runtime:  89.14%
# Memory:   90.20%


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            if node == None:
                continue

            if node.left == None and node.right == None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))



#------------------------------------------------------
# Solution 4 - Solution 3 w/o continue 
#------------------------------------------------------

# Runtime:  84.10%
# Memory:   86.26%


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            if node.left == None and node.right == None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))


#------------------------------------------------------
# Solution 5 - Solution 3 w/ deque 
#------------------------------------------------------

# Runtime:  67.56%
# Memory:   78.81%


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if node == None:
                continue

            if node.left == None and node.right == None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))


#------------------------------------------------------
# Solution 6 - Solution 5 w/o continue 
#------------------------------------------------------

# Runtime:  92.88%
# Memory:   91.67%


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if node.left == None and node.right == None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))