#------------------------------------------------------
# Solution 1 - recursive - flatten tree
#------------------------------------------------------

# Runtime:  84.24%
# Memory:   15.28%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = inf

        def flattenTree(root):
            if not root:
                return []

            result = []

            if root.left:
                result += flattenTree(root.left)

            result.append(root.val)

            if root.right:
                result += flattenTree(root.right)

            return result

        vals = flattenTree(root)
        for i in range(1, len(vals)):
            delta = vals[i] - vals[i - 1]
            result = min(result, delta)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/o ifs
#------------------------------------------------------

# Runtime:   7.17%
# Memory:   69.94%


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = inf

        def flattenTree(root):
            if not root:
                return []

            result = []

            result += flattenTree(root.left)

            result.append(root.val)

            result += flattenTree(root.right)

            return result

        vals = flattenTree(root)
        for i in range(1, len(vals)):
            delta = vals[i] - vals[i - 1]
            result = min(result, delta)

        return result


#------------------------------------------------------
# Solution 3 - Solution 2 compact
#------------------------------------------------------

# Runtime:  50.61%
# Memory:   15.28%


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = inf

        def flattenTree(root):
            if not root: return []
            
            result = []
            if root.left: result += flattenTree(root.left)
            result.append(root.val)
            if root.right: result += flattenTree(root.right)

            return result

        vals = flattenTree(root)
        for i in range(1, len(vals)):
            delta = vals[i] - vals[i - 1]
            result = min(result, delta)

        return result


#------------------------------------------------------
# Solution 4 - Solution 3 w/ custom min
#------------------------------------------------------

# Runtime:  29.95%
# Memory:   15.28%


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = inf

        def flattenTree(root):
            if not root: return []

            result = []
            if root.left: result += flattenTree(root.left)
            result.append(root.val)
            if root.right: result += flattenTree(root.right)

            return result

        vals = flattenTree(root)
        for i in range(1, len(vals)):
            delta = vals[i] - vals[i - 1]
            result = result if result < delta else delta

        return result


#------------------------------------------------------
# Solution 5 - Solution 4 w/ global Vals
#------------------------------------------------------

# Runtime:  63.69%
# Memory:   42.66%


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = inf

        vals = []

        def flattenTree(root):
            if not root: return

            if root.left: flattenTree(root.left)
            vals.append(root.val)
            if root.right: flattenTree(root.right)

        flattenTree(root)
        
        for i in range(1, len(vals)):
            delta = vals[i] - vals[i - 1]
            result = result if result < delta else delta

        return result


#------------------------------------------------------
# Solution 6 - Solution 5 w/ formatting changes
#------------------------------------------------------

# Runtime:  50.61%
# Memory:   15.28%


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = inf

        vals = []

        def flattenTree(root):
            if not root: 
                return

            if root.left: 
                flattenTree(root.left)

            vals.append(root.val)

            if root.right: 
                flattenTree(root.right)

        flattenTree(root)
        
        for i in range(1, len(vals)):
            delta = vals[i] - vals[i - 1]
            result = result if result < delta else delta

        return result


#------------------------------------------------------
# Solution 6 - Solution 1 w/o indexing
#------------------------------------------------------

# Runtime:  50.61%
# Memory:   42.66%


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = inf

        vals = []

        def flattenTree(root):
            if not root: 
                return

            if root.left: 
                flattenTree(root.left)

            vals.append(root.val)

            if root.right: 
                flattenTree(root.right)

        flattenTree(root)
        prev = vals[0]

        for val in vals[1:]:
            delta = val - prev
            prev = val
            result = result if result < delta else delta

        return result