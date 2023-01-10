#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  73.56%
# Memory:   72.95%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  93.78%
# Memory:   98.76%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = [(p, q)]

        while stack:
            nodes = stack.pop(0)

            if nodes[0] == None and nodes[1] == None:
                continue

            if nodes[0] == None or nodes[1] == None:
                return False

            if nodes[0].val != nodes[1].val:
                return False

            stack.append((nodes[0].left, nodes[1].left))
            stack.append((nodes[0].right, nodes[1].right))

        return True
