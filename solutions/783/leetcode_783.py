#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  56.88%
# Memory:   32.63%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def recurse(node) -> [int]:
            if not node:
                return []
            return recurse(node.left) + [node.val] + recurse(node.right)

        values = recurse(root)
        values.sort()


        result = inf

        for i in range(1, len(values)):
            delta = values[i] - values[i - 1]
            result = min(result, delta)
        
        return result



#------------------------------------------------------
# Solution 2 - recursive w/ early return
#------------------------------------------------------

# Runtime:  81.58%
# Memory:   74.83%



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def recurse(node) -> [int]:
            if not node:
                return []
            return recurse(node.left) + [node.val] + recurse(node.right)

        values = recurse(root)
        values.sort()


        result = inf

        for i in range(1, len(values)):
            delta = values[i] - values[i - 1]
            result = min(result, delta)
            if result == 1:
                return 1
        
        return result




#------------------------------------------------------
# Solution 3 - recursive w/ limited early return 1
#------------------------------------------------------

# Runtime:  35.31%
# Memory:   32.63%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def recurse(node) -> [int]:
            if not node:
                return []
            return recurse(node.left) + [node.val] + recurse(node.right)

        values = recurse(root)
        values.sort()


        result = inf

        for i in range(1, len(values)):
            delta = values[i] - values[i - 1]

            if result > delta:
                result = delta

                if result == 1:
                    return 1
        
        return result



#------------------------------------------------------
# Solution 4 - recursive w/ limited early return 2
#------------------------------------------------------

# Runtime:  81.58%
# Memory:   74.83%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def recurse(node) -> [int]:
            if not node:
                return []
            return recurse(node.left) + [node.val] + recurse(node.right)

        values = recurse(root)
        values.sort()


        result = inf

        for i in range(1, len(values)):
            delta = values[i] - values[i - 1]

            if delta < result:
                result = delta

                if result == 1:
                    return 1
        
        return result



#------------------------------------------------------
# Solution 5 - iterative w/ limited early return
#------------------------------------------------------

# Runtime:  92.70%
# Memory:   74.83%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        queue = [root]
        values = []

        while queue:
            node = queue.pop(0)

            if node:
                values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)


        values.sort()

        result = inf

        for i in range(1, len(values)):
            delta = values[i] - values[i - 1]

            if delta < result:
                result = delta

                if result == 1:
                    return 1
        
        return result