#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  49.55%
# Memory:   52.37%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Let's do the easy thing first: early returns
        if not root:
            return True

        if root.left == None and root.right == None:
            return True


        # Now...it's time to get recursive!

        def isSymmetricRecurse(left, right):
            # Always do the base cases first!
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False
            
            if left.val != right.val:
                return False

            # Now...the recursive case(s)

            outside = isSymmetricRecurse(left.left, right.right)
            inside = isSymmetricRecurse(left.right, right.left)

            return outside and inside


        # And finally, the call to start the whole thing going
        return isSymmetricRecurse(root.left, root.right)



#------------------------------------------------------
# Solution 2 - recursive (no comments)
#------------------------------------------------------

# Runtime:  70.21%
# Memory:   90.47%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left == None and root.right == None:
            return True

        def isSymmetricRecurse(left, right):
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False
            
            if left.val != right.val:
                return False

            return isSymmetricRecurse(left.left, right.right) and \
            isSymmetricRecurse(left.right, right.left)


        return isSymmetricRecurse(root.left, root.right)



#------------------------------------------------------
# Solution 3 - recursive (short name)
#------------------------------------------------------

# Runtime:  88.60%
# Memory:   90.47%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left == None and root.right == None:
            return True

        def isMirror(left, right):
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False
            
            if left.val != right.val:
                return False

            return isMirror(left.right, right.left) and isMirror(left.left, right.right)


        return isMirror(root.left, root.right)



#------------------------------------------------------
# Solution 4 - recursive (short name & reverse order)
#------------------------------------------------------

# Runtime:  92.87%
# Memory:   52.37%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left == None and root.right == None:
            return True

        def isMirror(left, right):
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False
            
            if left.val != right.val:
                return False

            return isMirror(left.left, right.right) and isMirror(left.right, right.left)


        return isMirror(root.left, root.right)