
#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  88.60%
# Memory:   49.77%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0

        # base case
        if root == None:
            return result

        # recursive case
        result = 1

        option_left = self.maxDepth(root.left)
        option_right = self.maxDepth(root.right)

        result += max(option_left, option_right)

        return result




#------------------------------------------------------
# Solution 2 - recursive (one line)
#------------------------------------------------------

# Runtime:  48.15%
# Memory:   18.14%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if root == None else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



#------------------------------------------------------
# Solution 3 - iterative
#------------------------------------------------------

# Runtime:  88.60%
# Memory:   81.30%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
            
        result = 0
        nodes = [root, None]
        
        while nodes:
            node = nodes.pop(0)

            if node == None:
                result += 1
                if len(nodes) > 0:
                    nodes += [None]
                continue

            if node.left:
                nodes += [node.left]

            if node.right:
                nodes += [node.right]

        return result


#------------------------------------------------------
# Solution 4 - recursive (best)
#------------------------------------------------------

# Runtime:  96.82%
# Memory:   76.15%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if root:
                return 1 + max(rec(root.left), rec(root.right))
            return 0

        return rec(root)